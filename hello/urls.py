from django.urls import path
from django.urls import re_path

from helloworld import views

urlpatterns = [
    path('', views.index),
    path('process/', views.process),
    path('form/', views.form),
    path('users/<str:name>/', views.users),
    re_path(r'', views.users),
]
