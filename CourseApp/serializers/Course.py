from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from CourseApp.models import Course


class CourseSerializer(serializers.ModelSerializer):
    image = SerializerMethodField()

    def get_image(self, course):
        request = self.context['request']
        name = course.image.name
        if name.startswith("static/"):
            path = '/%s' % name
        path = '/static/%s' % name

        return request.build_absolute_uri(path)

    class Meta:
        model = Course
        fields = ["id", "subject", "image", "created_date", "category"]
