from django.urls import path
from django.urls import re_path

from helloworld import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('process/', views.process),
    path('form/', views.form),
    re_path(r'', views.users),
]
