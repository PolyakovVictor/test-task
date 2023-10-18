from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'display'

urlpatterns = [
    path('', views.user_views, name='users'),
    path('add_user/', views.add_user_views, name='add_user'),
    path('groups/', views.group_views, name='groups'),
    path('add_group/', views.add_group_views, name='add_group'),
]
