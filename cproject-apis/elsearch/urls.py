from django.urls import path
from . import views

urlpatterns = [

    path("<str:qry>/<int:pg>/", views.search_q, name="search_q"),
    ]
