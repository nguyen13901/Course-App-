from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response

from CourseApp.models import Course
from CourseApp.models.pagination import CustomPagePagination
from CourseApp.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    serializer_class = CourseSerializer
    pagination_class = CustomPagePagination

    def get_queryset(self):
        courses = Course.objects.filter(active=True)

        q = self.request.query_params.get('q')
        if q is not None:
            courses = courses.filter(subject__icontains=q)

        cate_id = self.request.query_params.get('category_id')
        if cate_id is not None:
            courses = courses.filter(category_id=cate_id)
        return courses

    @action(detail=True, methods=['GET'], url_path='lessons')
    def get_lesson(self, request, pk):
        # course = Course.objects.get(pk=pk)
        course = self.get_object()
        lessons = course.lessons.filter(active=True)

        kw = request.query_params.get('kw')
        if kw is not None:
            lessons = lessons.filter(subject__icontains=kw)

        return Response(LessonSerializer(lessons, many=True).data, status=status.HTTP_200_OK)
