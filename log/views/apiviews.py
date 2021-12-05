from django.shortcuts import render
from rest_framework import viewsets

from ..serializers import *


class ResponseStatusLogViewSet(viewsets.ModelViewSet):
    queryset = ResponseStatusLog.objects.all().order_by('-id')
    serializer_class = ResponseStatusLogSerializer
