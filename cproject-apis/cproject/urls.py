"""cproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myauth/', include('myauth.urls')),
    path('search/', include('elsearch.urls')),
    path('get-books/', include('get_books.urls')),
    path('category/', include('get_books.urls')),
    path('get_bookinfo', include('isbn_bookinfo.urls')),
    path('cp_recommendation', include('cp_recommendation.urls')),
    path('product/', include('get_productinfo.urls')),
    path('pincode/', include('pincode.urls')),
    path('donation_form', include('donation_form.urls')),
    path('get_razorpayid', include('generate_razorpayid.urls')),
    path('user_orders/', include('user_orders.urls')),
    path('get_ordertrack_url', include('order_track.urls')),
    path('edit_address', include('edit_address.urls')),
    path('delete_address', include('delete_address.urls')),
    path('address_form', include('add_address.urls')),
    path('user_address', include('get_address.urls')),
    path('order_details', include('order_details.urls')),
    path('all_orders', include('all_orders.urls')),
    path('cancel_order', include('cancel_order.urls')),
    path('notify_me', include('book_notify.urls')),


]
