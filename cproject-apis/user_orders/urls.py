from django.urls import path
from . import views

urlpatterns = [
	
	path('<int:pg>/',views.UserOrder.as_view()),
	
	
	]