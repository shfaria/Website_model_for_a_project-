from ctypes import addressof
from django.shortcuts import render
from .models import Ipmodel, Project, New, Event
from django.http import HttpResponse
from hitcount.views import HitCountDetailView
from django.db.models import Q
# Create your views here.

from django.shortcuts import render
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from .models import Post

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'baseline.html'


class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'baseline.html'
    context_object_name = 'post'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': Post.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context


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