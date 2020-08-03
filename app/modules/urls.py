from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import User
from .models import Module

from . import views

urlpatterns = [
    # path('', views.get_module_data),
    # path('<int:module_id>/', views.ModuleView.as_view()),
    # path('<slug:slug>,<int:module_id>/', views.ModuleView.as_view()),
    # SETH
    path('<int:module_id>-<slug:slug>/', views.ModuleView.as_view()),
    path('<int:module_id>-<slug:slug>/student-page/', views.ModuleStudentView.as_view()),
]
