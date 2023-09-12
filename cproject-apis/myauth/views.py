from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
import re



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user :
            if user.is_active:
                login(request,user)
                data = {"code" : 200, "status" : "OK", "message" : "LogIn Successfull"}
                return JsonResponse(data)
            else:
                data = {"code" : 403, "status" : "Forbidden", "message" : "User Disabled"}
                return JsonResponse(data)
        else:
            data = {"code" : 401, "status" : "Unauthorized", "message" : "Invalid Login Credentials"}
            return JsonResponse(data)
    else:
        return render(request,'login.html')



# Django Rest Framework used
class logout(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = request.user
        token = Token.objects.get(user=user)
        if token:
            token.delete()
            data = {"code" : 200, "status" : "OK", "message" : "Log Out Successfull"}
            return Response(data)



def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('phone')
        password = request.POST.get('password')
        name = request.POST.get('name')
        email = request.POST.get('email')

        
        #validate whether the phone number is registered or not
        try:
            if User.objects.get(username = username):
                data = {"code" : 403, "status" : "Forbidden", "message" : "Entered Mobile Number is already registered. Try loggin-in"}
                return JsonResponse(data)
        
        except:
            pass


        #validate mobile number [must be 10 digits. assumed that all are of India, so ignored prefixed country codes]
        phoneregex = re.compile(r'^[1-9]\d{9}$')
        if phoneregex.search(str(username)):
            pass
        else:
            data = {"code" : 422, "status" : "Unprocessable Entity", "message" : "Mobile Number should be of 10 digits- ^[1-9]\d{9}$"}
            return JsonResponse(data)


        #validate name, making sure it is not empty
        firstregex = re.compile(r"^[A-Za-z][A-Za-z,.'].*$")
        if firstregex.search(str(name)):
            pass
        else:
            data = {"code" : 422, "status" : "Unprocessable Entity", "message" : "Name should start with an alphabet- ^[A-Za-z][A-Za-z,.']*$"}
            return JsonResponse(data)


        #validate email address
        emailregex = re.compile(r"^([\w\.\-]+)@([\w\-]+)((\.(\w){2,3})+)$")
        if str(email) != "":
            if emailregex.search(str(email)):
                pass
            else:
                data = {"code" : 422, "status" : "Unprocessable Entity", "message" : "Enter a valid email address- ^([\w\.\-]+)@([\w\-]+)((\.(\w){2,3})+)$"}
                return JsonResponse(data)


        #validate password
        passregex = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$")
        if passregex.search(str(password)):
            pass
        else:
            data = {"code" : 422, "status" : "Unprocessable Entity", "message" : "Password should be between 8 to 15 characters which contain at least one lowercase letter, one uppercase letter, one numeric digit, and one special character- ^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$"}
            return JsonResponse(data)


        authobj = User.objects.create_user(username = username, password = password, first_name = name, email = email)
        authobj.save()

        data = {"code" : 201, "status" : "Created", "message" : "Sign-Up Successfull"}
        return JsonResponse(data)


    else:
        return render(request,'user_signup.html')



# Django Rest Framework used
@api_view(['POST', ])
def get_token(request):
    if request.method == 'POST':
        username = request.data.get('phone')
        password = request.data.get('password')
        user = authenticate(username = username, password = password)
        if user :
            if user.is_active:
                tokened = Token.objects.filter(user=user)
                data = {}
                if tokened.count()>0:
                    data["code"] = 200
                    data["status"] = "OK"
                    data["message"] = "Token already Exists"
                    data["phone"] = username
                    data["Token"] = tokened[0].key
                    return Response(data)

                else:
                    token = Token.objects.create(user=user)
                    data["code"] = 201
                    data["status"] = "Created"
                    data["message"] = "Token Created"
                    data["Token"] = token.key
                    data["phone"] = username
                    return Response(data)
            else:
                data = {"code" : 403, "status" : "Forbidden", "message" : "User Disabled"}
                return Response(data)
        else:
            data = {"code" : 401, "status" : "Unauthorized", "message" : "Invalid Login Credentials"}
            return Response(data)
