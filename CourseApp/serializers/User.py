from rest_framework import serializers
from CourseApp.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name",
                  "username", "password", "email", "date_joined"]
        extra_kwargs = {
            'password': {"write_only": 'true'}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user