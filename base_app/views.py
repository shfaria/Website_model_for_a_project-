from django.shortcuts import render
from .models import Project
from django.http import HttpResponse
# Create your views here.


def home(request):
    everyproject = Project.objects.all()
    return render(request, 'base_app/home.html', {'everyproject': everyproject})



def directory(respose):
    return HttpResponse("<h1>directory</h1>")