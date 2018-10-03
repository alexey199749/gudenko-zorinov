from django.urls import path
from django.urls import re_path

from helloworld import views

urlpatterns = [
    re_path(r'^users/$', views.users),
    re_path(r'^users/(?P<name>\D+)/', views.users),
    re_path(r'', views.index),
]
