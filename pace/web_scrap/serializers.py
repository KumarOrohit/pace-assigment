from .models import WebScrapData
from rest_framework import serializers


class WebScrapDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebScrapData
        fields = '__all__'