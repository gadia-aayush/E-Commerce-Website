from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.Notify.as_view()),
	
	]
















