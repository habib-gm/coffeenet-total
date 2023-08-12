from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response
from .userSerializers import *
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError

# Create your views here.


@api_view(["POST"])
@permission_classes([AllowAny])
def createUser(request):
    data = request.data
    username = data["username"]
    password = data["password"]
    password = make_password(password)
    first_name = data["fullname"]
    try:
        User.objects.create(username=username, password=password, first_name=first_name)
        return Response(status=200)
    except Exception as e:
        if isinstance(e, IntegrityError):
            print("email exists")
            return Response("email already used", status=400)
        print(e)
        return Response(status=500)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def updatePassword(request):
    user = request.user
    newPassword = request.data["password"]
    password = make_password(newPassword)
    user.password = password
    try:
        user.save()
        return Response(status=200)
    except Exception as e:
        print(e)
        return Response(status=500)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getCurrUser(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)
