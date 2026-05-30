from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegisterForm
from courses.models import Course
from quiz.models import Result
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def register_user(request):

    form = RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account Created")
            return redirect('login')

    return render(request, 'users/register.html', {'form': form})


def login_user(request):

    if request.method == "POST":

        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user:
            login(request, user)
            return redirect('dashboard')

        messages.error(request, "Invalid Login")

    return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def dashboard(request):

    enrolled_courses = Course.objects.filter(students=request.user)
    results = Result.objects.filter(user=request.user)

    total_score = sum(r.score for r in results)

    return render(request, 'users/dashboard.html', {
        'enrolled_courses': enrolled_courses,
        'results': results,
        'total_score': total_score
    })



def profile(request):
    return render(request, 'users/profile.html')



@login_required(login_url='/users/login/')
def edit_profile(request):

    user = request.user

    if request.method == "POST":

        user.first_name = request.POST.get('first_name')
        user.email = request.POST.get('email')

        user.save()

        return redirect('profile')   # SAVE after redirect to profile

    return render(request, 'users/edit_profile.html')



