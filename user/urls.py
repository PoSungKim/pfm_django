from .views import UserListAPI, UserDetailAPI
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register),
    path('', UserListAPI.as_view()),
    path('<int:pk>', UserDetailAPI.as_view())
]
