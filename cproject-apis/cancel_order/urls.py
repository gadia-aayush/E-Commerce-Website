from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.CancelFlow.as_view()),

	]
















