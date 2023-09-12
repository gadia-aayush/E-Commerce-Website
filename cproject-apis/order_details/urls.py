from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.AddOrder.as_view()),
	
	]