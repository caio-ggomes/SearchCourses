from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Platform(models.Model):
    name = models.CharField(max_length=15, unique=True)
    evaluation = models.FloatField()

    def __str__(self):
        return self.name


class Course(models.Model):
    subject = models.CharField(max_length=31)
    name = models.CharField(max_length=63)
    difficulty = models.CharField(max_length=15)
    last_updated = models.DateTimeField(auto_now_add=True)
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='courses')
    duration = models.DurationField()
    description = models.TextField(max_length=2047)
    evaluation = models.FloatField()

    def __str__(self):
        return self.name


class Post(models.Model):
    message = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')