from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'last_name', 'middle_name', 'first_name', 'position']
