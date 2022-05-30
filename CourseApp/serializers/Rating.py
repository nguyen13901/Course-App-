from rest_framework import serializers

from CourseApp.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "rate", "created_date"]
