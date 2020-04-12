from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ReaderViewSet, BookViewSet, UserList

app_name='account'

router = SimpleRouter()
router.register(r'account', ReaderViewSet, basename="account")
router.register(r'book', BookViewSet, basename="book")
urlpatterns = router.urls
urlpatterns += [
    path('create/user/', UserList.as_view(), name="usercreate"),
]