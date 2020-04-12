from rest_framework import serializers
from .models import Reader


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Reader