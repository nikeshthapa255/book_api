from rest_framework import viewsets
from rest_framework import permissions
from .models import Reader
from .serializers import ReaderSerializer
from rest_framework.exceptions import PermissionDenied


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class ReaderViewSet(viewsets.ModelViewSet):
    serializer_class = ReaderSerializer
    permission_classes = (IsOwner, )

    # Ensure a user sees only own Reader objects.
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Reader.objects.filter(user=user)
        raise PermissionDenied()

    # Set user as owner of a Readers object.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
