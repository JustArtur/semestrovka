from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import *
from .forms import *

# Create your views here.


def home(request):
    user = request.user
    tasks = Task.objects.filter(user_id=user.id)
    context = {
        'tasks': tasks
    }
    return render(request,'home.html', context)


def create_task(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            try:
                task = Task()
                task.user_id = request.user
                # task.title = form.data['tittle']
                task.description = form.data['description']
                task.save()
                return redirect(f"/task/{task.id}")
            except Exception as err:
                form.add_error(None, err)
    else:
        form = TaskCreateForm()
    return render(request, 'create.html', {'form': form})


def show_task(requset, task_id):
    task = Task.objects.get(id=int(task_id))
    return render(requset, 'show.html', {'task': task})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                form.add_error(None, 'login')
                return redirect('/')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def show_user(request, user_id):
    return render(request, 'user_show.html')
