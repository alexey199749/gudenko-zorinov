from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UserForm
from .models import Process


def index(request):
    processes = Process.objects.all()
    return render(request, "index.html", {"processes": processes})


def create(request):
    if request.method == "POST":
        tom = Process()
        tom.proc_id = request.POST.get("proc_id")
        tom.name = request.POST.get("name")
        tom.user = request.POST.get("user")
        tom.save()
    return HttpResponseRedirect("/")


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
