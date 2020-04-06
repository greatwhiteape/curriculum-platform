from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers, serializers, viewsets
from rest_framework.parsers import JSONParser

from .models import Module # , Chapter

# @csrf_exempt
# def get_module_data(request):
# 	data = Module.objects.all().order_by('id')
# 	if request.method == 'GET':
# 		serializer = ModuleSerializer(data, many=True)
# 		return JsonResponse(serializer.data, safe=False)

# @csrf_exempt
# def get_chapter_data(request):
# 	data = Chapter.objects.all()
# 	if request.method == 'GET':
# 		serializer = ChapterSerializer(data, many=True)
# 		return JsonResponse(serializer.data, safe=False)

# class ProgramModulesView(ListView):
#     # model = Module
#     paginate_by = 1
#     template_name = 'modules/list.html'

#     def get_queryset(self):
#         self.modules = get_object_or_404(Module, program=3)
#         return Module.objects.filter(program='3')

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

# ViewSets define the view behavior.
# class ChapterViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Chapter.objects.all().order_by('id').reverse()
#     serializer_class = ChapterSerializer

# class ModuleViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Module.objects.all().order_by('id').reverse()
#     serializer_class=ModuleSerializer

# class LabVentureViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Module.objects.all().order_by('id').reverse()
#     serializer_class = ModuleSerializer