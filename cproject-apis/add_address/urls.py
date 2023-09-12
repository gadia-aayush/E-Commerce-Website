from django.urls import path
from . import views


urlpatterns = [
	
	path('', views.AddAddress.as_view()),

	]