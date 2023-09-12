from rest_framework import serializers
from .models import Donationreqs


class DonationreqsSerializer(serializers.ModelSerializer):
	class Meta:
		model= Donationreqs
		fields= '__all__'