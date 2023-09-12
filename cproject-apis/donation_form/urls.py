from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.AddDonation.as_view()),

 	]