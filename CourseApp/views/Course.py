from rest_framework import viewsets, generics

from CourseApp.models import Course
from CourseApp.models.pagination import CustomPagePagination
from CourseApp.serializers import CourseSerializer


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
