from django.contrib import admin
from .models import Subject, Platform, Course

# Register your models here.

admin.site.register(Subject)
admin.site.register(Platform)
admin.site.register(Course)
