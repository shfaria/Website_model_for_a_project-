from ctypes import addressof
from urllib import request
from django.shortcuts import render
from .models import Ipmodel, Project, New, Event
from django.http import HttpResponse
from django.db.models import Q
from itertools import chain
from django.template.loader import render_to_string




def home(request):
    everyproject = Project.objects.all()
    everynews = list(reversed(New.objects.all()))
    everyevent = list(reversed(Event.objects.all()))

    return render(request, 'base_app/home.html', {'everyproject': everyproject, 'everynews' : everynews, 'everyevent': everyevent})



def about(request):
    return render(request, 'base_app/about.html')

def activities(request):
    return render(request, 'base_app/activities.html')

def events(request):
    everyevent = list(reversed(Event.objects.all()))
    return render(request, 'base_app/events.html', {'everyevent': everyevent})

def news(request):
    everynews = list(reversed(New.objects.all()))
    return render(request, 'base_app/news.html',{ 'everynews' : everynews})

def faq(request):
    return render(request, 'base_app/faq.html')



def search(request):
    template_name= 'base_app/search_results.html'
    query = request.GET.get("q") 
    if query:
        projects = Project.objects.filter(Q(title__icontains=query) | Q(title__icontains=query),)
        events = Event.objects.filter(Q(title__icontains=query) | Q(title__icontains=query),)
        news = New.objects.filter(Q(title__icontains=query) | Q(title__icontains=query),)

        results = list(chain(projects, events, news))
        return render(request, template_name, {'results': results})

    else:
        results= []
        rendered = render_to_string('base_app/notfound.html', {'foo':'bar'})
        return HttpResponse(rendered)



   
    
    