from django.db.utils import OperationalError
from django.shortcuts import get_object_or_404
from .models import Subject, Platform, Difficulty, Duration, Language

subject_choices = list()
platform_choices = list()
difficulty_choices = list()
duration_choices = list()
language_choices = list()

try:
    for subject in Subject.objects.all():
        subject_choices.append((subject.name, subject.name))
    for platform in Platform.objects.all():
        platform_choices.append((platform.name, platform.name))
    for difficulty in Difficulty.objects.all():
        difficulty_choices.append((difficulty.name, difficulty.name))
    for duration in Duration.objects.all():
        duration_choices.append((duration.name, duration.name))
    for language in Language.objects.all():
        language_choices.append((language.name, language.name))
except OperationalError:
    pass
