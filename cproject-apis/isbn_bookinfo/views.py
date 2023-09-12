from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import *
from .models import  Books
import json, urllib.request


# view for searching the isbn & then retreiving the details
@api_view(['POST'])
def isbn_search(request):
	input_data = request.data.get('data')
	book_isbn = input_data["isbn"]

	query = Books.objects.filter(isbn= book_isbn)
	query_serializer = BooksSerializer(query, many=True)
	output_data = query_serializer.data

	if (len(output_data) != 0):
		#print ("mp-database")
		return Response ({"output" : output_data})		

	else:
		google_api_url= "https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(book_isbn)
		output_data= urllib.request.urlopen(google_api_url).read().decode()
		#print ("google books api")
		return HttpResponse(output_data)