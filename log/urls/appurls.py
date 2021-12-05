from django.urls import path
from django.urls import re_path

from ..views.appviews import *

app_name = 'log'

urlpatterns = [
    path('', LogListView.as_view(), name='list'),
    path('new/', LogCreateView.as_view(), name='new'),
    path('license/<int:pk>/edit/', LogUpdateView.as_view(), name='update'),
    path('license/<int:pk>/', LogDetailView.as_view(), name='detail'),
    path('license/<int:pk>/delete/', LogDeleteView.as_view(), name='delete'),

]
