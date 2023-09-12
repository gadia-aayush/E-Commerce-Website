from django.urls import path
from . import views

urlpatterns = [
	
	# for wallet balance
	path('', views.GetAddress.as_view()),
	
	]