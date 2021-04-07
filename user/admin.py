from django.contrib import admin
from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


# Admin Page에 모델 등록
admin.site.register(User, UserAdmin)
