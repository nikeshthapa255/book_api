from django.urls import path, include
from .views import registration

app_name='jwtauth'

urlpatterns = [
    path('register/', registration, name='register')
]