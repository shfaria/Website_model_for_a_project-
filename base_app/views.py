from ctypes import addressof
from django.shortcuts import render
from .models import Ipmodel, Project, New, Event
from django.http import HttpResponse
from hitcount.views import HitCountDetailView
from django.db.models import Q
# Create your views here.

def get_ip(request):
    address = request.META.get('HTTP_X_FORWARDED_FOR')
    if address:
        ip = address.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def home(request):
    everyproject = Project.objects.all()
    everynews = New.objects.all()
    everyevent = Event.objects.all()

    ip= get_ip(request)
    print(ip)
    anyip = Ipmodel(ip= ip)
    result= Ipmodel.objects.filter(Q(ip__icontains=anyip))

    if len(result) >= 1:
        print("exists")
    else:
        print("unique")

    count= Ipmodel.objects.all().count()
    print("total count", count)








    return render(request, 'base_app/home.html', {'everyproject': everyproject, 'everynews' : everynews, 'everyevent': everyevent, 'count': count})
















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