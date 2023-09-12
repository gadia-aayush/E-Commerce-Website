from django.shortcuts import render
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

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
from .models import Donationreqs
from .serializers import *
import json
from django.db import connection
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
import time, datetime



# view for adding donation form details to donationreqs table.
class AddDonation(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            input_time= int(time.time())
            #print (input_time)
            username = request.user  # fetching user_id
            #print (username)
            
            userid = User.objects.get(username = username).pk
            #print(userid)
    
            donor_data = request.data.get('data')
            #print (donor_data)

            model_use= Donationreqs()
            model_use.user_id= int(userid)
            model_use.volunteer_id= 0
            model_use.status= 1  #1- pending
            model_use.mobile= str(donor_data["mobile"])
            model_use.address= str(donor_data["address"])
            model_use.landmark= str(donor_data["landmark"])
            model_use.country= str(donor_data["country"])
            model_use.state= str(donor_data["state"])
            model_use.city= str(donor_data["city"])
            model_use.zipcode= int(donor_data["zipcode"])
            model_use.no_of_book= int(donor_data["no_of_book"])
            model_use.no_of_cartons= int(donor_data["no_of_cartons"])
            model_use.app_books_weight= float(donor_data["app_books_weight"])
            model_use.donated_book_category= str(donor_data["category"])
            model_use.how_do_u_know_abt_us= str(donor_data["source"])
            model_use.wastage = 0
            model_use.document_mail_sent= "N"
            model_use.is_blocked= "N"
            model_use.i_date= input_time
            model_use.u_date= input_time
            model_use.is_paid_donation= "N"
            model_use.donor_name= str(donor_data["donor_name"])
            model_use.pickup_date_time= str(donor_data["pickup_date"])
            model_use.save()

            message= "Donor Details of User Id- " + str(userid) + " , saved successfully."
            #print (message)
            return Response ({"status": 200, "message" : message}, status=status.HTTP_201_CREATED)

        except:
            return Response ({"status": 400, "message" : "failure- check readme"}, status=status.HTTP_400_BAD_REQUEST)