from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserForm


def index(request):
    return render(request, "index.html")


def process(request):
    return render(request, "process.html")


def form(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            process = userform.cleaned_data["process"]
            return HttpResponse("Hello {0}".format(process))
    return render(request, "form.html", {"form": userform})


def users(request, name="guest"):
    return HttpResponse("Hello {0}!".format(name))
