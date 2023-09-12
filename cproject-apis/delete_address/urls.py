from django.urls import path
from . import views


urlpatterns = [
	
	path('', views.DeleteAddress.as_view()),

	]