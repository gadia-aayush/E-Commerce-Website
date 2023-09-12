from django.shortcuts import render
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
# from .serializers import *
import json
from django.db import connection
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse

from django.contrib.auth.models import User

# Create your views here.
class DeleteAddress(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            addressid= request.data.get('address_id')
            cursor = connection.cursor()
            cursor.execute('''DELETE from useraddresses where address_id =%s''', addressid)
            message = "Address Deleted"
            #print (message)
            return Response ({"status": 200, "message" : message}, status=status.HTTP_202_ACCEPTED)

        except:
            return Response ({"status": 400, "message" : "failure- check readme"}, status=status.HTTP_400_BAD_REQUEST)