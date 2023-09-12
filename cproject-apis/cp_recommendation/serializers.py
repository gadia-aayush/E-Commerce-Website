from rest_framework import serializers
from .models import Orders, OrderAddress


class OrdersSerializer(serializers.ModelSerializer):
	class Meta:
		model= Orders
		fields= '__all__'


class OrderAddressSerializer(serializers.ModelSerializer):
	class Meta:
		model= OrderAddress
		fields= '__all__'