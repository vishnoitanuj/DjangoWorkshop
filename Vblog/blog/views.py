from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,HttpResponseRedirect,get_object_or_404,render_to_response
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import login,logout, get_user_model,authenticate
from .forms import *
from django.contrib import messages

# Create your views here.


def index_view(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs,
        "home_title" : "Home"
    }
    return render(request, "index.html", context)

def about_view(request):
    about = About_Us.objects.all()
    context = {
        "about_us" : about,
        "home_title" : "About-Us"
    }

    return render(request, "about.html", context)

# def blog_create(request):
#     form = BlogForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         return HttpResponseRedirect(instance.get_absolute_url())
#     context = {
#         "form": form,
#     }
#     return render(request,"home/innovation_form.html", context)
#
#
# def blog_update(request, pk=None):
#     instance = get_object_or_404(Innovation,pk=pk)
#     form = InnovationForm(request.POST or None, request.FILES or None, instance=instance)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         return HttpResponseRedirect(instance.get_absolute_url())
#
#     context = {
#         "title":instance.title,
#         "instance":instance,
#         "form": form,
#     }
#     return render(request, "home/innovation_form.html", context)
#
#
# def blog_delete(request, pk=None):
#     instance = get_object_or_404(Innovation, pk=pk)
#     instance.delete()
#     messages.success(request,"Successfully Deleted")
#     return redirect("home:innovation")
