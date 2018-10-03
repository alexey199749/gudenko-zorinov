from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")

def users(request, name = ""):
    output = "Hello {0}".format(name)
    return HttpResponse(output)