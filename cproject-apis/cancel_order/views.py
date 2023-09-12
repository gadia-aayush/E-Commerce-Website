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
from .models import  Bookinventory, Books, Orders, OrderBooks
from .serializers import *
from django.db import connection
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
import json



# this will execute the entire cancellation flow.
class CancelFlow(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		input_time= int(time.time())
		input_data = request.data.get('data')
		cancel_order_id= input_data["order_id"]
		print (cancel_order_id)

		cursor = connection.cursor()
		cursor.execute('''SELECT status FROM orders WHERE order_id= %s ''', cancel_order_id)
		order_status= [x[0] for x in cursor][0]
		print (type(order_status))
		print (order_status)

		if (int(order_status) == 0):
			print ("Cancellation Possible")

			# changing the order status to cancelled
			cancel_row= Orders.objects.get(order_id= cancel_order_id)
			cancel_row.status= 2
			cancel_row.u_date= input_time
			cancel_row.save()

			# fetching the cancelled order's- book_inv_id's
			cursor.execute('''SELECT book_inv_id FROM order_books WHERE order_id= %s ''', cancel_order_id)
			cancel_inv_ids= [x[0] for x in cursor]
			print (cancel_inv_ids)

			# increasing the book qty & changing its stock status
			for book_inv in cancel_inv_ids:
				try:
					book_inv_row= Bookinventory.objects.get(book_inv_id= int(book_inv))
					if (book_inv_row.is_soldout == "Y"):
						book_inv_row.is_soldout = "N"
						book_inv_row.u_date= input_time
						book_inv_row.save()

					cursor.execute('''SELECT book_id FROM bookinventory WHERE book_inv_id= %s ''', book_inv)
					cancel_book_id= [x[0] for x in cursor][0]
					#print (cancel_book_id)
					book_row= Books.objects.get(book_id= cancel_book_id)

					if (book_row.is_out_of_stack == "Y"):
						#print (book_row.is_out_of_stack)
						book_row.is_out_of_stack = "N"

					#print (book_row.qty)
					book_row.qty= book_row.qty+1  #assuming each book, despite of same book_id are allotted different rows in order_books
					book_row.u_date= input_time
					#print (book_row.qty)
					book_row.save()

				except:
					return Response({"status" : 400, "message" : "Cancellation Unsuccessful- Contact Admin"})					

			return Response({"status" : 200, "message" : "Cancellation Successful"})

		else:
			return Response({"status" : 200, "message" : "Cancellation Not Allowed"})