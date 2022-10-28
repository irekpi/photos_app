from rest_framework import serializers
from app.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
        read_only_fields = ('width', 'height', 'main_color')


class JsonSerializer(serializers.Serializer):
    json_file = serializers.FileField()

    class Meta:
        fields = ['json_file']
