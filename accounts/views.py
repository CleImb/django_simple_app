from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class UserDetail(LoginRequiredMixin, APIView):
    """Allow logged user to get his profil infos and to patch it."""

    def get(self, request):
        return render(
            request,
            "accounts/user_detail.html",
            {"user": request.user},
        )

    def patch(self, request):
        user = User.objects.get(pk=request.user.id)
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
