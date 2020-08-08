from django.contrib import admin
from .models import Subject, Platform, Course, Difficulty, Duration

# Register your models here.

admin.site.register(Subject)
admin.site.register(Platform)
admin.site.register(Course)
admin.site.register(Difficulty)
admin.site.register(Duration)
