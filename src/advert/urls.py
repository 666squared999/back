from rest_framework.routers import DefaultRouter
from .views import AdvertViewSet
from django.urls import path
from .views import (
    PhotoView,
)

urlpatterns = [
    path("photos/", PhotoView.as_view(), name="photo"),
]

router = DefaultRouter()
router.register('adverts', AdvertViewSet, basename='adverts')

urlpatterns = urlpatterns + router.urls