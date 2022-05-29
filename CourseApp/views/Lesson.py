from django.http import Http404
from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response

from CourseApp.models import Lesson, Tag
from CourseApp.serializers import LessonDetailSerializer, TagSerializer


class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonDetailSerializer

    @action(detail=True, methods=['POST'], url_path='tags')
    def add_tags(self, request, pk):
        try:
            lesson = self.get_object()
        except Http404:
            return Response({"error_massage": "Lesson is not exist"}, status=status.HTTP_404_NOT_FOUND)
        else:
            tags = request.data.get("tags")
            if tags is not None:
                for tag in tags:
                    t, _ = Tag.objects.get_or_create(name=tag)
                    lesson.tags.add(t)
                lesson.save()
                return Response(LessonDetailSerializer(lesson).data, status=status.HTTP_201_CREATED)
        return Response({"error_massage": "Tag's information is not valid"}, status=status.HTTP_400_BAD_REQUEST)
