from django.conf.urls import url
from .import views
from django.views.generic.dates import ArchiveIndexView
from .models import *
from .import views as core_views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^about/$', views.about_view, name='about_us'),
    ]
