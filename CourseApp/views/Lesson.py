from typing import Union

from django.db.models import F
from django.http import Http404
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from CourseApp.models import Lesson, Tag, Comment, Action, Rating, LessonView
from CourseApp.serializers import LessonDetailSerializer, TagSerializer
from CourseApp.serializers.Action import ActionSerializer
from CourseApp.serializers.Comment import CommentSerializer
from CourseApp.serializers.LessonView import LessonViewSerializer
from CourseApp.serializers.Rating import RatingSerializer


class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonDetailSerializer

    def get_permissions(self):
        if self.action in ["add_comments", "take_action", "rating"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

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

    @action(detail=True, methods=['POST'], url_path="comments")
    def add_comments(self, request, pk):
        content = request.data.get('content')
        if content:
            c = Comment.objects.create(content=content,
                                       lesson=self.get_object(),
                                       creator=request.user)

            return Response(CommentSerializer(c).data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["POST"], url_path="like")
    def take_action(self, request, pk):
        try:
            action_type = int(request.data['type'])
        except (IndexError, ValueError):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            action = Action.objects.create(type=action_type,
                                           lesson=self.get_object(),
                                           creator=request.user)
            return Response(ActionSerializer(action).data,
                            status=status.HTTP_200_OK)

    @action(detail=True, methods=["POST"], url_path="rating")
    def rate(self, request, pk):
        try:
            rating = int(request.data['rating'])
        except (IndexError, ValueError):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            r = Rating.objects.create(rate=rating,
                                      lesson=self.get_object(),
                                      creator=request.user)
            return Response(RatingSerializer(r).data,
                            status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True, url_path="views")
    def incr_view(self, request, pk):
        v, created = LessonView.objects.get_or_create(lesson=self.get_object())
        v.views = F('views') + 1
        v.save()
        v.refresh_from_db()

        return Response(LessonViewSerializer(v).data, status=status.HTTP_200_OK)