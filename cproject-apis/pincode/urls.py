from django.urls import path
from . import views

urlpatterns = [

    # path('', views.search, name=""),
    path("cod_check/<int:pin>/", views.cod_check, name="cod_check"),
    path("pin_check/<int:pin>/", views.pin_check, name="pin_check"),
#    path('/product/<product_id>/', 'product_detail_view', name='product_detail')
    ]
