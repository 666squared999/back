from rest_framework import viewsets
from rest_framework import permissions
from advert.serializers import AdvertSerializer
from advert.models import Advert


class AdvertViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = [permissions.IsAuthenticated]
