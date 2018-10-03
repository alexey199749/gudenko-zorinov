from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserForm


def index(request):
    return render(request, "index.html")


def users(request, name="guest"):
    output = "Hello {0}!".format(name)
    return HttpResponse(output)


def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse("Hello {0}!".format(name))
    elif request.method == "GET":
        return render(request, "form.html", {"form": UserForm()})
