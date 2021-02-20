from rest_framework import serializers
from advert.models import Advert

class AdvertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advert
        fields = ['title', 'photo_urls', 'animal_type', 'breed', 'color', 'sex', 'description']