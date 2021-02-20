from rest_framework import serializers
from users.serializers import UserSerializer
from advert.models import Advert, Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = (
            'advert',
            'photo_url'
        )


class CreateAdvertSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Advert
        fields = '__all__'
        read_only_fields = ['id', 'user',]

    def create(self, validated_data):
        user = self.context['request'].user
        advert = Advert.objects.create(user=user, **validated_data)
        advert.save()
        return advert


class RetrieveAdvertSerializer(CreateAdvertSerializer):
    user = UserSerializer()
    photos = PhotoSerializer(many=True)
