from django.urls import path
from django.urls import re_path

from helloworld import views

urlpatterns = [
    path('', views.process),
    path('process/', views.process),
    re_path(r'', views.users),
]
