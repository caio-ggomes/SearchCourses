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
    courses_names = list()
    if search.platform == 'Udemy':
        [courses_links, courses_names] = scraper.udemy()
    elif search.platform == 'edX':
        [courses_links, courses_names] = scraper.edx()
    elif search.platform == 'Coursera':
        [courses_links, courses_names] = scraper.coursera()
    elif search.platform == 'Qualquer Plataforma':
        [courses_links, courses_names] = scraper.all()
    courses = list()
    i = 0
    for course_link in courses_links:
        try:
            course = Course.objects.get(link=course_link)
            course.name = courses_names[i]
        except:
            course = Course(
                name=courses_names[i],
                subject=search.subject,
                platform=search.platform,
                difficulty=search.difficulty,
                duration=search.duration,
                language=search.language,
                link=course_link,
            )
            course.save()
        courses.append(course)
        i += 1
    return render(request, 'courses_list.html', {'courses': courses})

def search_course(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save(commit=False)
            search.save()
            return redirect('courses_list', search_id=search.id)
    else:
        form = SearchForm() 
    return render(request, 'search_form.html', {'form': form})
        