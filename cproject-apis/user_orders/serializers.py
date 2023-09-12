from rest_framework import serializers
from .models import Books, OrderBooks, Orders


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model= Books
        fields= '__all__'   


class OrderBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model= OrderBooks
        fields= '__all__'  


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model= Orders
        fields= '__all__' 