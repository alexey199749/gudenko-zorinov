from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def users(request, name=""):
    output = "Hello {0}".format(name)
    return HttpResponse(output)