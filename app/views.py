from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, parser_classes
from rest_framework.parsers import JSONParser
from app.serializers import PhotoSerializer, JsonSerializer
from app.models import Photo
from scripts.client import PhotoClient
from scripts.file_client import FilePhotoClient

URL = 'https://jsonplaceholder.typicode.com/photos'


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class ExternalPhotoViewSet(viewsets.ViewSet):
    """
    Class to get photos from external url or file source (Json added only)
    Additional args added to "simulate" dependency injection
    """

    serializer_class = JsonSerializer
    photo_client = PhotoClient()
    file_photo_client = FilePhotoClient()

    @action(detail=False, methods=['get'], url_path='url')
    def url(self, request) -> Response:
        """
        Get data with custom request client and check response inside custom Client class
        Validation is done by Pydantic model
        """
        response = self.photo_client.get(URL)
        if not response:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(response, status.HTTP_200_OK)

    @parser_classes([JSONParser])
    @action(detail=False, methods=['post'], url_path='json')
    def json(self, request) -> Response:
        """
        External class to parse data
        """
        print(request)
        data = self.file_photo_client.parse(request.data['json_file'].read())
        if not data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status.HTTP_200_OK)
