from wagtail.api.v2.endpoints import BaseAPIEndpoint
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Module #, Chapter
from .serializers import ModuleSerializer #, ChapterSerializer


class ModulesViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer