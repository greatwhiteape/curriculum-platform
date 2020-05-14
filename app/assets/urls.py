from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import User
from .models import Asset

from . import views

urlpatterns = [
    # path('', views.get_module_data),
    path('<int:asset_id>/', views.AssetView.as_view()),
    path('<int:asset_id>/student-page/', views.AssetStudentView.as_view()),
]
