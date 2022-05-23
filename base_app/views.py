from django.shortcuts import render
from .models import Project, New, Event
from django.http import HttpResponse
# Create your views here.

# from hitcount.models import HitCount
# from hitcount.views import HitCountMixin

# first get the related HitCount object for your model object
# hit_count = HitCount.objects.get_for_object(Project)

# next, you can attempt to count a hit and get the response
# you need to pass it the request object as well
# hit_count_response = HitCountMixin.hit_count(request, hit_count)





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



