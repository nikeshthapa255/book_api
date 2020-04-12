from rest_framework import serializers
from .models import Reader, Book
from django.contrib.auth.models import User



class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ( 'id', 'user' ,'books')
        model = Reader

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'id', 'genre', 'amazon_url')
        model = Book

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', 'username')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Reader.objects.create(user = user)
        print('CREATED - ', user)
        return user

   