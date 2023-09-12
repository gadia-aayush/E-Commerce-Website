from rest_framework import serializers
from .models import Booknotify, Books


class BooknotifySerializer(serializers.ModelSerializer):
	class Meta:
		model= Booknotify
		fields= '__all__'


class BooksSerializer(serializers.ModelSerializer):
	class Meta:
		model= Books
		fields= '__all__'

