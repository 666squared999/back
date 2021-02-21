from rest_framework.routers import DefaultRouter
from .views import AdvertViewSet
from django.urls import path
from .views import (
    PhotoView, MailView
)

urlpatterns = [
    path('photos/', PhotoView.as_view(), name='photo'),
    path('mail/', MailView.as_view(), name='mail'),
]

router = DefaultRouter()
router.register('adverts', AdvertViewSet, basename='adverts')

urlpatterns = urlpatterns + router.urls