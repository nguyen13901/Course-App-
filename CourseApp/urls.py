from django.urls import path, include
from rest_framework import routers
from CourseApp import views

router = routers.DefaultRouter()
router.register("categories", views.CategoryViewSet, basename='category')
router.register("courses", views.CourseViewSet, basename="course")
router.register("lessons", views.LessonViewSet, basename='lessons')

urlpatterns = [
    path("", include(router.urls)),
]
