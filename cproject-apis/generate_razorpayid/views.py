from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import views
import razorpay
from rest_framework import status


# this will generate razorpay_id for both order_id as well as donationreq_id.
@api_view(['POST'])
def generate_razorpayid(request):
    input_data = request.data.get('data')
    mp_ref_id= str(input_data["ref_id"])
    bill_amount= float(input_data["amount"])
    client= razorpay.Client(auth=("rzp_live_pvrJGzjDkVei3G", "lV126EaCs37zRLeYJ6Zdrb6t"))
    params = {"amount" : bill_amount,"currency":"INR","payment_capture": True, "receipt": mp_ref_id}
    razorpay_response= client.order.create(data= params)
    razorpayid= razorpay_response["id"]
    output= {"rp_id": razorpayid}
    return Response ({"status" : 200, "message" : "success", "output": output}, status=status.HTTP_201_CREATED)