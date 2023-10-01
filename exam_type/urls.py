from django.urls import path
from . import views

urlpatterns = [
    path('exam_add/', views.ExamAdd, name='exam_add'),
    path('exam_list/', views.ExamList, name='exam_list'),
    path('exam_update/<str:exam_name>', views.ExamUpdate, name='exam_update'),
    path('exam_delete/<str:exam_name>', views.ExamDelete, name='exam_delete'),
]