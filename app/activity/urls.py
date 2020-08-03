from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import User
from .models import Activity

from . import views

urlpatterns = [
    # path('', views.get_module_data),
    path('<int:activity_id>-<slug:slug>/', views.ActivityView.as_view()),
    path('<int:activity_id>-<slug:slug>/student-page/', views.ActivityStudentView.as_view()),
]
