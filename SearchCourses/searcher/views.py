from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SearchForm
from .models import Course, Platform, Subject, Search, Difficulty, Duration
from .scrapers import Scraper

def home(request):
    if request.method == 'POST':
        return redirect('search_form')
    return render(request, 'home.html')

def courses_list(request, search_id):
    search = get_object_or_404(Search, id=search_id)
    scraper = Scraper(
        subject=search.subject,
        language=search.language,
        duration=search.duration,
        difficulty=search.difficulty,
    )
    courses_links = list()
    if search.platform == 'Udemy':
        courses_links = scraper.udemy()
    if search.platform == 'edX':
        courses_links = scraper.edx()
    if search.platform == 'Coursera':
        courses_links = scraper.coursera()
    courses = list()
    for course_link in courses_links:
        course = Course.objects.get(link=course_link)
        if(course.DoesNotExist):
            course = Course(
                subject=search.subject,
                platform=search.platform,
                difficulty=search.difficulty,
                duration=search.duration,
                language=search.language,
                link=course_link,
            )
            course.save()
        courses.append(course)
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
        
