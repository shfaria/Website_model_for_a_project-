from django.shortcuts import render
from .models import Project, New, Event
from django.http import HttpResponse
# Create your views here.


def home(request):
    everyproject = Project.objects.all()
    everynews = New.objects.all()
    everyevent = Event.objects.all()
    return render(request, 'base_app/home.html', {'everyproject': everyproject, 'everynews' : everynews, 'everyevent': everyevent})

def about(request):
    return render(request, 'base_app/about.html')



def directory(respose):
    return HttpResponse("<h1>directory</h1>")