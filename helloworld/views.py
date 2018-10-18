from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

from helloworld.forms import UserForm
from helloworld.models import Process


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

def edit(request, id):
    try:
        process = Process.objects.get(id=id)
        if request.method == "POST":
            process.proc_id = request.POST.get("proc_id")
            process.name = request.POST.get("name")
            process.user = request.POST.get("user")
            process.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"process": process})
    except Process.DoesNotExist:
        return HttpResponseNotFound("<h2>Process not found</h2>")

def delete(request, id):
    try:
        process = Process.objects.get(id=id)
        process.delete()
        return HttpResponseRedirect("/")
    except Process.DoesNotExist:
        return HttpResponseNotFound("<h2>Process not found</h2>")


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
