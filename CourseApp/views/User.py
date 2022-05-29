from django.conf import settings
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from CourseApp.models import User
from CourseApp.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer()

    def get_permissions(self):
        if self.action == "get_current_user":
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path="current-user")
    def get_current_user(self, request):
        return Response(UserSerializer(request.user).data,
                        status=status.HTTP_200_OK)


class AuthInfo(APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)
