from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import User
from .models import Module
# from rest_framework import routers
from .views import ModuleViewSet

from .endpoints import ModulesViewSet

from . import views

urlpatterns = [
    path('', views.get_module_data),
    path('<int:module_id>/', views.ModuleView.as_view()),
    path('<int:module_id>/student-page/', views.ModuleStudentView.as_view()),
]