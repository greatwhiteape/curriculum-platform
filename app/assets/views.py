from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers, serializers, viewsets
from rest_framework.parsers import JSONParser

from .models import Asset

# @csrf_exempt
class AssetsView(TemplateView):
    template_name = "assets/search_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assets'] = serialize('json',Asset.objects.all())
        return context

class AssetView(TemplateView):
    template_name = "assets/asset_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['asset'] = Asset.objects.get(id=kwargs['asset_id'])
        return context

class AssetStudentView(TemplateView):
    template_name = "assets/student_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['asset'] = Asset.objects.get(id=kwargs['asset_id'])
        return context
