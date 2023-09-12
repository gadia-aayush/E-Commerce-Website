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

from django.contrib.auth.models import User

from rest_framework import status
from .models import Useraddresses
import json
from django.db import connection
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse


# view for adding form details to database table.
class EditAddress(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
	        username = request.user  # fetching user_id
	        userid = User.objects.get(username = username).pk
	        #print (userid)
	        address_data = request.data.get('data')
	        #print (address_data)

	        cursor = connection.cursor()
	        cursor.execute('''UPDATE useraddresses SET title= %s, rec_name= %s, pincode= %s, address= %s, landmark= %s, phone_no= %s, is_primary= %s,
	        				state_name= %s, city_name= %s, country_name= %s WHERE address_id= %s and user_id= %s''', (str(address_data["title"]), str(address_data["rec_name"]),
	        				int(address_data["pincode"]), str(address_data["address"]), str(address_data["landmark"]), 	str(address_data["phone_no"]), str(address_data["is_primary"]),
	        				str(address_data["state_name"]), str(address_data["city_name"]), str(address_data["country_name"]), str(address_data["address_id"]), userid))

	        message= "Address of User Id- " + str(userid) + " , updated successfully."
	        #print (message)
	        return Response ({"status": 200, "message" : message}, status=status.HTTP_201_CREATED)

        except:
            return Response ({"status": 400, "message" : "failure- check readme"}, status=status.HTTP_400_BAD_REQUEST)