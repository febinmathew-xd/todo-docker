from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .form import MyUserCreationForm
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

@login_required(login_url='login')
def home(request):
    page = 'home'
    
    todos = Todo.objects.filter(user=request.user)

    context = {
        'page':page,
        'todos':todos
    }



    return render(request, 'pages/home.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    page = 'login'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist :
            messages.error(request, 'user not found')
            return redirect('login')
        
        user = authenticate(request,username=user, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'wrong password')
            return redirect('login')





    context = {'page':page}

    return render(request, 'pages/login.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    page = 'signup'
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'failed')
        


    context = {'page':page}   
        
    return render(request, 'pages/signup.html', context)


@login_required(login_url='login')
def logout_user(request):
    
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def add_todo(request):
    user = request.user
    task = request.POST.get('task')
    if task :
        todo = Todo.objects.create(user=user, task=task)
        todo.save()
    return redirect('home')


@login_required(login_url='login')
def delete_todo(request, pk):

    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        raise Http404('todo doesnot exist')
    
    if request.user == todo.user:
        todo.delete()
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required(login_url='login')
def finish_todo(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        raise Http404('todo doesnot exits')

    if request.user == todo.user:
        todo.is_active = not todo.is_active
        todo.save()
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))



    

