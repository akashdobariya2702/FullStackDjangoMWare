from django.db import models


class ResponseStatusLog(models.Model):
    json_response = models.JSONField(default=dict)

    class Meta:
        verbose_name = "Response Status Log"
        verbose_name_plural = "Response Status Logs"
