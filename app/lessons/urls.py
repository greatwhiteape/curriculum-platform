from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.get_lessons_data),
    path('<int:lesson_id>-<slug:slug>/', views.LessonView.as_view()),
    path('<int:lesson_id>-<slug:slug>student-page/', views.LessonStudentView.as_view()),
]
