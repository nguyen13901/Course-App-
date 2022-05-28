from rest_framework import viewsets, generics

from CourseApp.models import Category
from CourseApp.serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

