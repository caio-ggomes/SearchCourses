from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SearchForm
from .models import Course, Platform, Subject, Search, Difficulty, Duration

def home(request):
    return render(request, 'home.html')

def courses_list(request, search_id):
    search = get_object_or_404(Search, id=search_id)
    courses = Course.objects.all().filter(
        subject=get_object_or_404(Subject, name=search.subject),
        platform=get_object_or_404(Platform, name=search.platform),
        difficulty=get_object_or_404(Difficulty, name=search.difficulty),
        duration=get_object_or_404(Duration, name=search.duration)
    )
    return render(request, 'courses_list.html', {'courses': courses})

def search_course(request):
    user = User.objects.first() # TODO: get the currently logged in user
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save(commit=False)
            search.created_by = user
            search.save()
            return redirect('courses_list', search_id=search.id)
    else:
        form = SearchForm() 
    return render(request, 'search_form.html', {'form': form})
        
