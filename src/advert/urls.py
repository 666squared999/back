from rest_framework.routers import DefaultRouter
from .views import AdvertViewSet
from django.urls import path


router = DefaultRouter()
router.register('adverts', AdvertViewSet, basename='adverts')

urlpatterns = router.urls