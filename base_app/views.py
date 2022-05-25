from ctypes import addressof
from django.shortcuts import render
from .models import Ipmodel, Project, New, Event
from django.http import HttpResponse






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
    everyevent = Event.objects.all()
    return render(request, 'base_app/events.html', {'everyevent': everyevent})

def news(request):
    everynews = New.objects.all()
    return render(request, 'base_app/news.html',{ 'everynews' : everynews})

def faq(request):
    return render(request, 'base_app/faq.html')