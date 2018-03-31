from django.db import models

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.urlresolvers import reverse


class Blog(models.Model):
    author = models.CharField(max_length= 250)
    title = models.CharField(max_length=250)
    image = models.FileField(blank=True, default='msc.png')
    width_field=models.IntegerField(default=0)
    height_field=models.IntegerField(default=0)
    detail = models.TextField(blank=True)
    updatedtime = models.DateField(auto_now=True, auto_now_add=False)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    tag = models.CharField(max_length=50, blank=True, default='guest')

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk': self.pk})

    def __str__(self):
        return self.author+' - '+self.title

    class Meta:
        ordering = ["-updatedtime","-timestamp"]

class About_Us(models.Model):
    image = models.FileField(blank=True, default='logo_text.png')
    description = models.TextField()
    check = models.BooleanField(default=False)
