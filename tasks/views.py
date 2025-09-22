from django.shortcuts import render , redirect , get_object_or_404
from .models import Task
from django.http import HttpResponse
from .forms import TaskForm
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required



@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-id')
    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context  )


@login_required
def home(request):
    return redirect('tasks:task_list')


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False) 
            task.user = request.user      
            task.save() 
            return redirect('tasks:task_list') 
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'ffform': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})



def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  
            user.save()
            login(request, user)
            messages.success(request, "خوش آمدی. ثبت‌نام با موفقیت انجام شد.")
            return redirect("tasks:task_list")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})



@require_http_methods(["GET", "POST"])

def logout_now(request):
    logout(request)
    next_url = request.GET.get('next') or request.POST.get('next') or reverse('tasks:task_list')
    return redirect(next_url)



def welcome(request):
    # اگر قبلا لاگین شده، مستقیماً بفرستش داخل برنامه
    if request.user.is_authenticated:
        return redirect('tasks:task_list')
    # در غیر این صورت صفحه خوش‌آمد نمایش بده
    return render(request, 'tasks/welcome.html', {
        'login_url': reverse('tasks:login'),
        'next_url': reverse('tasks:task_list'),
    })






