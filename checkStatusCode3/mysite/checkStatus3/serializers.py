from rest_framework import serializers
from .models import CheckUrl, UrlError




class UrlErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlError
        fields = ('status', 'url', 'checkUrl')

class CheckUrlSerializer(serializers.ModelSerializer):
    error = UrlErrorSerializer(many=True)
    class Meta:
        model = CheckUrl
        fields = ('id', 'test', 'time', 'error')

class CheckUrl2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CheckUrl
        fields = ('id', 'test', 'time')