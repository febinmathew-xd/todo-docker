from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .form import MyUserCreationForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login_page(request):
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
            messages.error(request, 'username or password doesnot exit')
            return redirect('login')





    context = {'page':page}

    return render(request, 'pages/login.html', context)


def signup(request):
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
        


        
        
    return render(request, 'pages/signup.html', {'form':form})



def logout_user(request):
    
    logout(request)
    return redirect('login')