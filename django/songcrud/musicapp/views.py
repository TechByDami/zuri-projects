from django.http import HttpResponse


def index(request):
    return HttpResponse("My first music app")
