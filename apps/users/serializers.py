from rest_framework import serializers

from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "password", "email", "first_name", "last_name","role"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()

        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = [
            "id",
            "groups",
            "user_permissions",
            "is_staff",
            "is_superuser",
            "last_login",
            "password",
            "date_joined",
            "is_active",
        ]
