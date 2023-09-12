from rest_framework import serializers
from .models import  Bookinventory, Books, Orders, OrderBooks


class BookinventorySerializer(serializers.ModelSerializer):
	class Meta:
		model= Bookinventory
		fields= '__all__'


class BooksSerializer(serializers.ModelSerializer):
	class Meta:
		model= Books
		fields= '__all__'


class OrdersSerializer(serializers.ModelSerializer):
	class Meta:
		model= Orders
		fields= '__all__'


class OrderBooksSerializer(serializers.ModelSerializer):
	class Meta:
		model= OrderBooks
		fields= '__all__'				