from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Blog)
class BlogAdminModel(admin.ModelAdmin):
    list_display = ["author","title","timestamp"]
    list_filter = ["timestamp"]

admin.site.register(About_Us)
