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
from .models import Booknotify, Books
from .serializers import *
import json
from django.db import connection
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse


# class for adding the book notify details to database table.
class Notify(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            username = request.user  # fetching user_id
            userid = User.objects.get(username = username).pk
            #print (userid)
            #print ("check-1")
            input_data = request.data.get('data')
            #print  (input_data)

            # extracting book details
            query = Books.objects.filter(slug= input_data["slug"])
            query_serializer = BooksSerializer(query, many=True)
            query_data = query_serializer.data
            query_json = json.dumps(query_data)
            query_dict = json.loads(query_json)[0]
            #print (query_dict)

            # extracting user email
            useremail = User.objects.get(username = username).email
            #print (useremail)

            model_use= Booknotify()
            model_use.bookid= query_dict["book_id"]
            model_use.user_id= int(userid)
            model_use.user_email= str(useremail)
            model_use.book_name= str(query_dict["title"])
            model_use.isbn= str(query_dict["isbn"])
            model_use.is_mail_sent= "N"
            model_use.save()

            message= "Notification of Book Title- " + str(query_dict["title"]) + " , added successfully."
            print (message)
            return Response ({"status": 200, "message" : message}, status=status.HTTP_201_CREATED)

        except:
            return Response ({"status": 400, "message" : "failure- check readme"}, status=status.HTTP_400_BAD_REQUEST)
