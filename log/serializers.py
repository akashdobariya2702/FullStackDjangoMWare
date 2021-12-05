# python library

# django library
from rest_framework import serializers

from .models import *


class ResponseStatusLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseStatusLog
        fields = '__all__'
