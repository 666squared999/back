from rest_framework import viewsets
from rest_framework import permissions
from advert.serializers import AdvertSerializer
from advert.models import Advert
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AdvertViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination
