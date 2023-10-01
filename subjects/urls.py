from django.urls import path
from . import views

urlpatterns = [
     path('create_subject/<str:class_name>', views.SubjectsAdd, name='subjects_add'),
    path('list_subject/<str:class_name>', views.SubjectsList, name='subjects_list'),
    path('delete_subject/<str:class_name>/<str:subjects_name>',views.SubjectsDelete,name='subjects_delete'),
    path('update_subject/<str:class_name>/<str:subjects_name>',views.SubjectsUpdate,name='subjects_update'),

]