from url.models import UrlData
from rest_framework import serializers

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlData
        fields = ("url",)

class ShortUrlListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlData
        fields = "__all__"