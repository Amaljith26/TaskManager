from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Task, TaskCategory
from .forms import TaskForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

class IndexPageView(TemplateView):
    template_name = 'index.html'

def create_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('name')
        task_description = request.POST.get('description')
        task_status = request.POST.get('status')

        # Create the new task
        task = Task(
            name=task_name,
            description=task_description,
            status=task_status
        )
        task.save()

        return redirect('task_manager')  

    return render(request, 'index.html')


def task_manager(request):
    if request.user.is_authenticated:
        tasks_in_progress = Task.objects.filter(status='in-progress')
        tasks_completed = Task.objects.filter(status='completed')
        tasks_pending = Task.objects.filter(status='pending')
    else:
        # If the user is not authenticated, show empty task lists
        tasks_in_progress = []
        tasks_completed = []
        tasks_pending = []

    context = {
        'tasks_in_progress': tasks_in_progress,
        'tasks_completed': tasks_completed,
        'tasks_pending': tasks_pending,
    }
    
    return render(request, 'index.html', context)


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_manager')




def Signuppage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validate passwords
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
        else:    
            user = User.objects.create_user(username=username, password=password1, email=email)
            user.first_name = name
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')

    return render(request, 'signup.html')



def Loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('task_manager') 
        else:
            messages.error(request, "Invalid username or password!")
    return render(request, 'login.html')

def Logoutpage(request):
    logout(request)
    return redirect('task_manager')

