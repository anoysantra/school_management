from django.urls import path
from . import views

urlpatterns = [
    path('session_add/', views.SessionAdd, name='session_add'),
    path('session_list/', views.SessionList, name='session_list'),
    path('session_update/<str:session_name>', views.SessionUpdate, name='session_update'),
    path('session_delete/<str:session_name>', views.SessionDelete, name='session_delete'),
]