from rest_framework import serializers

from CourseApp.models import Action


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ["id", "type", "created_date"]
        