from django.shortcuts import render
from todolist.models import Task
from todolist.forms import TaskForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user_logged_in = request.user
    task = Task.objects.filter(user=user_logged_in)
    context = {
        'todolist': task,
        'user': user_logged_in,
    }
    return render(request, 'todolist.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
    
@login_required(login_url='/todolist/login')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login')
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            task = Task(title=title, description=description, user=user)
            task.save()
            return redirect('todolist:show_todolist')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()

    return render(request, 'create-task.html', {'form': form})

@login_required(login_url='/todolist/login/')
def not_done_task(request, id):
    user = request.user
    TaskData = Task.objects.filter(user=user).get(pk=id)
    TaskData.is_finished = False
    TaskData.save()
    return HttpResponseRedirect(reverse("todolist:show_todolist")) 

@login_required(login_url='/todolist/login/')
def done_task(request, id):
    user = request.user
    TaskData = Task.objects.filter(user=user).get(pk=id)
    TaskData.is_finished = True
    TaskData.save()
    return HttpResponseRedirect(reverse("todolist:show_todolist")) 

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    user = request.user
    TaskData = Task.objects.filter(user=user).get(pk=id)
    TaskData.delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist")) 