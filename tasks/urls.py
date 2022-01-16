from django.contrib import admin
from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.index),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('tasks/', views.IndexView.as_view(), name='tasks'),
    path('add/', views.add, name='add'),
    path('<int:pk>/', views.TaskView.as_view(), name='task'),
]
