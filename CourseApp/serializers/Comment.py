from rest_framework import serializers

from CourseApp.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "created_date", "updated_date"]
