from rest_framework import serializers
from .models import Orders, OrderAddress, Useraddresses


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model= Orders
        fields= '__all__'


class OrderAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model= OrderAddress
        fields= '__all__'        


class UseraddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Useraddresses
        fields= '__all__'   