from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers, serializers, viewsets
from rest_framework.parsers import JSONParser

from .models import Activity

# @csrf_exempt
class ActivitiesView(TemplateView):
    template_name = "activity/search_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activity'] = serialize('json',Activity.objects.all())
        return context

class ActivityView(TemplateView):
    template_name = "activity/activity_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activity'] = Activity.objects.get(id=kwargs['activity_id'])
        return context

class ActivityStudentView(TemplateView):
    template_name = "activity/student_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activity'] = Activity.objects.get(id=kwargs['activity_id'])
        return context
