from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from .models import Reader, Book
from django.contrib.auth.models import User
from .serializers import ReaderSerializer, BookSerializer, UserSerializer
from rest_framework.exceptions import PermissionDenied


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class ReaderViewSet(viewsets.ModelViewSet):
    serializer_class = ReaderSerializer
    permission_classes = (IsOwner, )
    # queryset = Reader.objects.all()
    # Ensure a user sees only own Reader objects.
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Reader.objects.filter(user = user)
        raise PermissionDenied()

    # Set user as owner of a Readers object.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = (IsOwner, )
    # Ensure a user sees his books only.
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated :
            try:
                user.reader
            except :
                raise PermissionDenied()
            return Book.objects.filter(author=user.reader)
        raise PermissionDenied()

    # Set user as owner of a Readers object.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user.reader)

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

