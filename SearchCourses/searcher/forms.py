from django import forms
from .models import Search
from .choices import *

class SearchForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget = forms.Select(choices=subject_choices)
        self.fields['platform'].widget = forms.Select(choices=platform_choices)
        self.fields['difficulty'].widget = forms.Select(choices=difficulty_choices)
        self.fields['duration'].widget = forms.Select(choices=duration_choices)
        self.fields['language'].widget = forms.Select(choices=language_choices)
    
    class Meta:
        model = Search
        fields = ['subject', 'platform', 'difficulty', 'duration', 'language']