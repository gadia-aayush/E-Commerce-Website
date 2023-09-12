from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import views
from .models import Orders, OrderAddress
from .serializers import *
import json, requests


# this view will return the clickpost recommendation of courier partners
@api_view(['POST'])
def fetch_recommendation(request):
    input_data = request.data.get('data')
    orderid = input_data["order_id"]
    weight=  input_data["weight"]  #clickpost takes weight in grams.
    # print (input_data, orderid, weight)

    try:
        # querying orders table
        query_1= Orders.objects.filter(order_id= orderid)
        query_1_serializer = OrdersSerializer(query_1, many=True)
        query_1_data = query_1_serializer.data
        query_1_json = json.dumps(query_1_data)
        query_1_dict = json.loads(query_1_json)[0]
        amount= query_1_dict["amount"]

        if (query_1_dict["payusing"]== "cod"):
            order_type= "COD"
        else:
            order_type= "PREPAID"


        # querying orderaddress table
        query_2= OrderAddress.objects.filter(order_id= orderid)
        query_2_serializer = OrderAddressSerializer(query_2, many=True)
        query_2_data = query_2_serializer.data
        # print (query_2_data) # check this output
        query_2_json = json.dumps(query_2_data)
        # print (query_2_json)
        query_2_dict = json.loads(query_2_json)[0]
        pincode= query_2_dict["pincode"]


        # preparing data to be sent
        payload= [{"pickup_pincode" : "700136", "drop_pincode": str(pincode), "order_type": str(order_type),
                    "reference_number": str(orderid), "item": "books", "invoice_value": float(amount), 
                    "delivery_type": "FORWARD","weight": float(weight)}]
        final_payload = json.dumps(payload)
        # print (final_payload)


        # calling clickpost recommendation api
        url = "https://www.clickpost.in/api/v1/recommendation_api/"
        querystring = {"key":"1e96edab-1b4b-440b-894f-63a2d42e2be0"} # api key
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, data=final_payload, headers=headers, params=querystring)
        # print (json.loads(response.text))
        return Response ({"status": response.status_code, "output" : json.loads(response.text), "reason": response.reason})
        
    except:
        return Response({"status" : 400, "message" : "failure- check with readme"},status=status.HTTP_400_BAD_REQUEST)    
