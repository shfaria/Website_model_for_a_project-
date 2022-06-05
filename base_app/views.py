from ctypes import addressof
from urllib import request
from django.shortcuts import render
from .models import Ipmodel, Project, New, Event
from django.http import HttpResponse
from django.db.models import Q
from itertools import chain
from django.views.generic import TemplateView, ListView








def home(request):
    everyproject = Project.objects.all()
    everynews = list(reversed(New.objects.all()))
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





class Search(ListView):
    model = Ipmodel, Project, New, Event
    template_name = 'base_app/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get("q") 
        cities =  Project.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query),
        ) 
        foods =  New.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query),
        )
        object_list = chain(cities, foods)
        return object_list
 