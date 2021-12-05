from django.conf import settings
from django.http import JsonResponse

from .models import *


def LoggingMiddleware(get_response):
    def middleware(request):
        response = get_response(request)

        if response.status_code in settings.LOG_STATUS_CODE:
            data = {
                'status_code': response.status_code,
                'error': str(response.content),
            }
            ResponseStatusLog.objects.create(
                json_response=data
            )

            return JsonResponse(data)

        return response

    return middleware
