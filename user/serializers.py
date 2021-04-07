from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:  # table명
        model = User
        fields = '__all__'

    