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
from .models import  Useraddresses
from .serializers import *
from rest_framework import status
import json


# this will fetch all the addresses of a user.
class GetAddress(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
    	try:
	    	username = request.user  # fetching user_id
	    	userid = User.objects.get(username = username).pk
	    	#print (userid)
	    	query = Useraddresses.objects.filter(user_id= userid)
	    	#print (query)
	    	query_serializer = UseraddressesSerializer(query, many=True)
	    	query_data = query_serializer.data
	    	query_json = json.dumps(query_data)
	    	query_list = json.loads(query_json)
	    	return Response ({"status" : 200, "message" : "success", "output": query_list}, status=status.HTTP_201_CREATED)    

    	except:
    		return Response({"status" : 400, "message" : "failure- check readme", "output" : "null"},status=status.HTTP_400_BAD_REQUEST)