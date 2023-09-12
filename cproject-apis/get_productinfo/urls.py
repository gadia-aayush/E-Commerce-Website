from django.urls import path
from . import views

urlpatterns = [
	
	# for /product link, it will fetch all the books
	path('<int:pg>/',views.all_books),
	

	# for each individual product
	path('<slug:slug>',views.product_details),
	
	]