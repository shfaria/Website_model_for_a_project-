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

def activities(request):
    return render(request, 'base_app/activities.html')

def events(request):
    return render(request, 'base_app/events.html')

def news(request):
    return render(request, 'base_app/news.html')

def faq(request):
    return render(request, 'base_app/faq.html')



