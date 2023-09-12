from rest_framework import serializers
from .models import  Useraddresses


class UseraddressesSerializer(serializers.ModelSerializer):
	class Meta:
		model= Useraddresses
		fields= '__all__'	