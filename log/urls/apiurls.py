# python library

# django library
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

# project library
from ..views.apiviews import *

router = DefaultRouter()

# app urls
router.register(r'logs', ResponseStatusLogViewSet, basename='logs')

urlpatterns = [
    url(r'^', include(router.urls)),
]
