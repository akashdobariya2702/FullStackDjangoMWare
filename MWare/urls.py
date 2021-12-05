from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('log.urls.apiurls', 'api_log'), namespace='api_log')),
    path('', include('log.urls.appurls')),
]
