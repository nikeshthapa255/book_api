from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ReaderViewSet

app_name='account'

router = SimpleRouter()
router.register('account', ReaderViewSet, basename="account")
urlpatterns = router.urls