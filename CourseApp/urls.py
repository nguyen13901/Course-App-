from django.urls import path, include
from rest_framework import routers
from CourseApp import views

router = routers.DefaultRouter()
router.register("", views.CategoryViewSet, basename='category')

urlpatterns = [
    path("", include(router.urls)),
]
