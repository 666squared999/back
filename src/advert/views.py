from rest_framework import viewsets
from rest_framework import permissions
from advert.serializers import (
    CreateAdvertSerializer,
    RetrieveAdvertSerializer,
    PhotoSerializer
)
from advert.models import Advert, Photo
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from src.email import send_mail

def modify_input_for_multiple_files(advert, photo_url):
    dict = {}
    dict['advert'] = advert
    dict['photo_url'] = photo_url
    return dict


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AdvertViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Advert.objects.all()
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['breed', 'sex', 'color', 'animal_type']

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return RetrieveAdvertSerializer
        else:
            return CreateAdvertSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user', None)
        if user:
            return Advert.objects.filter(user=user)
        else:
            return Advert.objects.all()


class PhotoView(APIView):
    def get(self, request):
        advert = request.query_params.get('advert', None)
        if advert:
            all_photos = Photo.objects.filter(advert=advert).all()
            serializer = PhotoSerializer(all_photos, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return Response(
                {"detail":"advert param is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, *args, **kwargs):
        advert = request.data['advert']

        # converts querydict to original dict
        photo_urls = dict((request.data).lists())['photo_url']
        flag = 1
        arr = []
        for photo_url in photo_urls:
            modified_data = modify_input_for_multiple_files(
                advert,
                photo_url,
            )
            file_serializer = PhotoSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                flag = 0

        if flag == 1:
            return Response(arr, status=status.HTTP_201_CREATED)
        else:
            return Response(arr, status=status.HTTP_400_BAD_REQUEST)


class MailView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            email = request.user.email
        else:
            email = request.data.get('to')
            
        if email is None: 
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        send_mail('lol', 'kek', email)
        return Response({}, status=status.HTTP_200_OK)
        