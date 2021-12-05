from django.urls import path
from django.urls import re_path

from apps.store.views.appviews import *

app_name = 'store'

urlpatterns = [
    path('', LicenseListView.as_view(), name='license_home'),
    path('license/new/', UserLicenseTemplateView.as_view(), name='license_new'),
    path('license/<slug:slug>/', LicenseDetailView.as_view(), name='license_details'),
    path('license/<slug:slug>/edit/', LicenseUpdateView.as_view(), name='license_update'),
]
