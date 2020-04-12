from django.contrib import admin

from .models import Reader, Book

# Register your models here.
admin.site.register(Reader)
admin.site.register(Book)