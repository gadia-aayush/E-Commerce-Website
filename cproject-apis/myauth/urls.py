from django.urls import path
from . import views


urlpatterns = [

    # path('', views.search, name=""),
    path("login/", views.user_login, name="user_login"),
    path('logout/', views.logout.as_view(), name='logout'),
    path("signup/",views.user_signup,name = "user_signup"),
    path("get-token/", views.get_token, name="get_token"),
    ]
