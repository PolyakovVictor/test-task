from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'display'

urlpatterns = [
    path('', views.user_views, name='users'),
    path('add_user/', views.add_user_views, name='add_user'),
    path('user_edit/<int:user_id>/', views.user_edit_views, name='user_edit'),
    path('user_delete/<int:user_id>/', views.user_delete_views, name='user_delete'),
    path('groups/', views.group_views, name='groups'),
    path('add_group/', views.add_group_views, name='add_group'),
    path('group_edit/<int:group_id>/', views.group_edit_views, name='group_edit'),
    path('group_delete/<int:group_id>/', views.group_delete_views, name='group_delete'),
]
