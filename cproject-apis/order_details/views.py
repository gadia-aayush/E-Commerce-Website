from django.shortcuts import render
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import views
from datetime import date
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


from rest_framework import status
from .models import Orders, OrderAddress, Useraddresses
from .serializers import *
import time, datetime, json
from django.db import connection
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse

from django.contrib.auth.models import User


# view for adding order details to database table.
class AddOrder(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            order_time= int(time.time())
            input_date= datetime.datetime.today().strftime('%Y-%m-%d')
            
            username = request.user  # fetching user_id
            userid = User.objects.get(username = username).pk #fetching user_id
            #print (userid)
            orders_data = request.data.get('data')
            print (orders_data)

            model_use= Orders()
            model_use.user_id= int(userid)
            model_use.amount= float(orders_data["amount"])
            model_use.no_of_book= int(orders_data["no_of_book"])
            model_use.status= "NA"
            model_use.payusing= str(orders_data["payusing"])
            model_use.biiling_add_id= int(orders_data["billing_add_id"])
            model_use.shipping_add_id= int(orders_data["shipping_add_id"])
            model_use.status = int(orders_data["status"])
            model_use.i_by= 0
            model_use.i_date= order_time
            model_use.u_by= 0
            model_use.u_date= order_time
            model_use.is_thanks_mail_sent= "N"
            model_use.is_notification_sent = "N"

            try:
                model_use.fast_delivery= int(orders_data["fast_delivery"])
            except:
                model_use.fast_delivery= 0

            try:
                model_use.shipping_handling_donation= float(orders_data["shipping_handling_donation"])
            except:
                model_use.shipping_handling_donation= 0

            try:
                model_use.prepaid_discount= int(orders_data["prepaid_discount"])
            except:
                model_use.prepaid_discount= 0

            try:
                model_use.delivery_charge_newbooks= int(orders_data["delivery_charge_newbooks"])
            except:
                model_use.delivery_charge_newbooks= 0

            model_use.cod_charge= 0

            try:
                model_use.coupon_id= str(orders_data["coupon_id"])
                model_use.coupon_amount= float(orders_data["coupon_amount"])
            except:
                model_use.coupon_id= "null"
                model_use.coupon_amount= 0

            model_use.cod_offer_interested= 0
            model_use.actual_date_upload= str(input_date)

            try:
                model_use.wallet_used= float(orders_data["wallet_used"])
            except:
                model_use.wallet_used= 0

            model_use.save()
            add_orderaddressdb(userid, int(orders_data["shipping_add_id"]) , order_time)

            message= "Order Details of Order booked by User Id- " + str(userid) + " , added successfully."
            #print (message)
            return Response ({"status": 200, "message" : message}, status=status.HTTP_201_CREATED)


        except:
            return Response ({"status": 400, "message" : "failure- check readme"}, status=status.HTTP_400_BAD_REQUEST)



# view for adding order address to "orderaddress" table    
def add_orderaddressdb(userid, shippingid, ordertime):
    #print (userid, shippingid, ordertime)
    query_1= Orders.objects.filter(user_id= userid, shipping_add_id= shippingid, i_date= ordertime)
    query_1_serializer = OrdersSerializer(query_1, many=True)
    query_1_data = query_1_serializer.data

    query_1_json = json.dumps(query_1_data)
    #print (query_1_json)
    query_1_dict = json.loads(query_1_json)[0]  #since only 1 row will come as output
    orderid= query_1_dict["order_id"]

    query_2= Useraddresses.objects.filter(address_id= shippingid)
    query_2_serializer = UseraddressesSerializer(query_2, many=True)
    query_2_data = query_2_serializer.data
    query_2_json = json.dumps(query_2_data)
    query_2_dict = json.loads(query_2_json)[0]  #since only 1 row will come as output

    # inserting data in orderaddress table
    model_use_2= OrderAddress()
    model_use_2.order_id= int(orderid)
    model_use_2.rec_name= str(query_2_dict["rec_name"])
    model_use_2.pincode= int(query_2_dict["pincode"])
    model_use_2.address= str(query_2_dict["address"])
    model_use_2.landmark= str(query_2_dict["landmark"])
    model_use_2.city= str(query_2_dict["city_name"])
    model_use_2.country= str(query_2_dict["country_name"])
    model_use_2.state= str(query_2_dict["state_name"])
    model_use_2.phone= str(query_2_dict["phone_no"])
    model_use_2.i_date= ordertime
    model_use_2.save()
