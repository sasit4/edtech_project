from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Category
from django.db.models import Q
from django.contrib import messages

def course_list(request):

    query = request.GET.get('q', '').strip()
    category = request.GET.get('category')

    courses = Course.objects.all()

    if query:
        courses = courses.filter(title__icontains=query)

    if category:
        courses = courses.filter(category__id=category)

    categories = Category.objects.all()

    return render(request, 'courses/courses.html', {
        'courses': courses,
        'categories': categories
    })


def course_details(request, id):

    course = get_object_or_404(Course, id=id)

    related_courses = Course.objects.filter(
        category=course.category
    ).exclude(id=course.id)[:3]

    return render(request, 'courses/details.html', {
        'course': course,
        'related_courses': related_courses
    })


def enroll_course(request, id):

    if not request.user.is_authenticated:
        return redirect('login')

    course = Course.objects.get(id=id)
    course.students.add(request.user)

    messages.success(request, "Enrolled Successfully")
    return redirect('course_details', id=id)


def watch_course(request, id):

    course = Course.objects.get(id=id)

    return render(request, 'courses/watch.html', {
        'course': course
    })