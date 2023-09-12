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
from .models import Useraddresses
from .serializers import *
import json
from django.db import connection
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse

from django.contrib.auth.models import User


# view for adding form details to database table.
class AddAddress(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            username = request.user  # fetching user_id
            userid = User.objects.get(username = username).pk
            #print (userid)
            address_data = request.data.get('data')
            #print (address_data)

            model_use= Useraddresses()
            model_use.user_id= int(userid)
            model_use.title= str(address_data["title"])
            model_use.rec_name= str(address_data["rec_name"])
            model_use.pincode= int(address_data["pincode"])
            model_use.address= str(address_data["address"])
            model_use.landmark= str(address_data["landmark"])
            model_use.phone_no= str(address_data["phone_no"])
            model_use.address_type= 0
            model_use.is_primary= str(address_data["is_primary"])
            model_use.state_name= str(address_data["state_name"])
            model_use.city_name= str(address_data["city_name"])
            model_use.country_name= str(address_data["country_name"])
            model_use.save()

            message= "Address of User Id- " + str(userid) + " , added successfully."
            #print (message)
            return Response ({"status": 200, "message" : message}, status=status.HTTP_201_CREATED)

        except:
            return Response ({"status": 400, "message" : "failure- check readme"}, status=status.HTTP_400_BAD_REQUEST)

