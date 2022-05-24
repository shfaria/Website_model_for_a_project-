from django.db import models
from django.forms import CharField
from django.db import models
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    published = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to= 'base_app/images/')
    url = models.URLField(blank= True) 

    def __str__(self):
        return self.title


class New(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to= 'base_app/images/')
    url = models.URLField(blank= True) 

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    # image = models.ImageField(upload_to= 'base_app/images/')
    url = models.URLField(blank= True) 

    def __str__(self):
        return self.title


class Ipmodel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip