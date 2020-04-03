from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers, serializers, viewsets
from rest_framework.parsers import JSONParser
from lessons.models import Lesson
from lessons.serializers import LessonSerializer

@csrf_exempt
def get_lessons_data(request):
	data = Lesson.objects.all()
	if request.method == 'GET':
		serializer = LessonSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)

# Create your views here.
# ViewSets define the view behavior.
class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class=LessonSerializer

class LessonView(TemplateView):
    template_name = "lessons/lesson_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = Lesson.objects.get(id=kwargs['lesson_id'])
        return context

class LessonStudentView(TemplateView):
    template_name = "lessons/student_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = Lesson.objects.get(id=kwargs['lesson_id'])
        return context