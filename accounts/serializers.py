from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "school", "bio"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"].lower(),  # normalize here too
            email=validated_data.get("email"),
            password=validated_data["password"]
        )

class LowercaseTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        attrs["username"] = attrs["username"].lower()
        return super().validate(attrs)
