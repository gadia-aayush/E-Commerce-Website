from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
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

from .serializers import *
from .models import Books, OrderBooks, Orders
import json
from django.db import connection
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse



# this will fetch user's order details.
class UserOrder(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pg):
        username = request.user  # fetching user_id
        userid = User.objects.get(username = username).pk
        start= (int(pg)-1)*10
        cursor = connection.cursor()
        cursor.execute('''select t1.order_id, t1.amount, t1.no_of_book, t1.actual_date_upload, t1.status, t1.payusing, t1.i_date, title, thumb, price from 
    					  (select orders.order_id, user_id, amount, no_of_book, actual_date_upload, status, payusing, i_date, book_id from orders inner join order_books 
    					  on orders.order_id = order_books.order_id where user_id= %s) t1 inner join books on t1.book_id= books.book_id order by t1.i_date desc limit %s,10''', (userid, start))
        rows = [x for x in cursor]
        cols = [x[0] for x in cursor.description]
    	# print (rows)

        all_orders= []
        for each_row in set(rows):
            each_order= {}
            for i in range(len(cols)):
                each_order[cols[i]]= each_row[i]
    		# print (each_order )
            all_orders.append(each_order)

    	# print (all_orders)
        final_dict= {"status" : 200, "message" : "success", "output": all_orders}
        final_json = json.dumps(final_dict)
        return HttpResponse (final_json)