from django.contrib import admin
from .models import Project, Event, New

# Register your models here.
admin.site.register(Project)
admin.site.register(Event)
admin.site.register(New)

