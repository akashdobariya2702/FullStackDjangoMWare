from django import forms

from .models import *


class ResponseStatusLogForm(forms.ModelForm):
    class Meta:
        model = ResponseStatusLog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ResponseStatusLogForm, self).__init__(*args, **kwargs)
        self.fields['json_response'].initial = {
            'status_code': 200,
            'error': ''
        }
