from django.contrib import admin
from django.urls import path, include
from user.views import UserListAPI, UserDetailAPI

# /admin/* 이러한 형태의 주소는 모두 admin 페이지로 간다
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
]
