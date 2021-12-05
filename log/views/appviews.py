from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse

from ..models import *
from ..forms import *


class LogListView(ListView):
    model = ResponseStatusLog
    queryset = ResponseStatusLog.objects.all().order_by('-id')
    template_name = 'log/log_list.html'
    extra_context = {
        'title': 'Log',
    }

    def get_queryset(self):
        return ResponseStatusLog.objects.all().order_by('-id')


class LogCreateView(CreateView):
    model = ResponseStatusLog
    form_class = ResponseStatusLogForm
    template_name = 'log/log_form.html'
    extra_context = {
        'title': 'Create Log',
        'submit_btn_text': 'Create',
    }

    def get_success_url(self, *args, **kwargs):
        return reverse("log:list")


class LogUpdateView(UpdateView):
    model = ResponseStatusLog
    form_class = ResponseStatusLogForm
    template_name = 'log/log_form.html'
    extra_context = {
        'title': 'Update Log',
        'submit_btn_text': 'Update',
    }

    def get_success_url(self, *args, **kwargs):
        return reverse("log:list")


class LogDetailView(DetailView):
    model = ResponseStatusLog
    queryset = ResponseStatusLog.objects.all()
    template_name = "log/log_detail.html"
    extra_context = {
        'title': 'Log Detail',
    }


class LogDeleteView(DeleteView):
    model = ResponseStatusLog
    template_name = "log/log_delete.html"

    def get_success_url(self):
        return reverse("log:list")
