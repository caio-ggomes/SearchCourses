from django.db.utils import OperationalError
from django import forms
from .models import Course, Subject, Platform, Search
from .choices import *

class SearchForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget = forms.Select(choices=subject_choices)
        self.fields['platform'].widget = forms.CheckboxSelectMultiple(choices=platform_choices)
        self.fields['difficulty'].widget = forms.CheckboxSelectMultiple(choices=difficulty_choices)
        self.fields['duration'].widget = forms.CheckboxSelectMultiple(choices=duration_choices)
    
    class Meta:
        model = Search
        fields = ['subject', 'platform', 'difficulty', 'duration']