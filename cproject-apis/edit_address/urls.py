from django.urls import path
from . import views


urlpatterns = [
	
	path('', views.EditAddress.as_view()),

	]