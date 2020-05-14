from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers, serializers, viewsets
from rest_framework.parsers import JSONParser

from .models import Module

# @csrf_exempt
class ModulesView(TemplateView):
    template_name = "modules/search_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modules'] = serialize('json',Module.objects.all())
        return context

class ModuleView(TemplateView):
    template_name = "modules/module_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module'] = Module.objects.get(id=kwargs['module_id'])
        return context

class ModuleStudentView(TemplateView):
    template_name = "modules/student_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module'] = Module.objects.get(id=kwargs['module_id'])
        return context
