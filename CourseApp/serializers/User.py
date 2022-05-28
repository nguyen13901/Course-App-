from rest_framework import serializers
from CourseApp.models import User


class User(serializers.ModelSerializer):
    model = User
    fields = "__all__"
