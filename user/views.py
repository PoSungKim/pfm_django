from .models import User
from django.http import HttpResponse
from django.core import serializers
from .serializers import UserSerializer
from rest_framework import mixins, generics
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password


class UserListAPI(generics.GenericAPIView) :
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs) :
        self.queryset = User.objects.raw("SELECT * FROM User")
        dataJSON = serializers.serialize('json', self.queryset)
        print(request)
        print(dataJSON)
        return HttpResponse(dataJSON, content_type="text/json-comment-filtered")

class UserDetailAPI(generics.GenericAPIView) :
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs) :
        self.queryset = User.objects.raw("SELECT * FROM User WHERE id = %s", str(kwargs['pk']))
        dataJSON = serializers.serialize('json', self.queryset)
        print(dataJSON)
        return HttpResponse(dataJSON, content_type="text/json-comment-filtered")


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        #username = request.POST['username']
        username = request.POST.get('username', None)

        #password = request.POST['password']
        password = request.POST.get('password', None)

        #rePassword = request.POST['re-password']
        rePassword = request.POST.get('re-password', None)

        responseData = {}

        if not (username and password and rePassword):
            responseData['error'] = "모두 기입해주십시오"

        elif (password != rePassword):
            responseData['error'] = "비밀번호가 다릅니다"

        else:
            user = User(username=username, password=make_password(password))
            user.save()

        return render(request, 'register.html', responseData)
