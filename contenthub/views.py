from django.shortcuts import render, redirect
from django.http import JsonResponse
import re
from .models import Content
from django.conf import settings
from . import cron

# for authentication
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


'''
    @login_required decorator specifies user must be logged in before accessing the view functino
    The argument (login_url="login") redirects the user to the login page if not logged in
    homepage view renders the homepage with the random 18 contents of the database
'''

@login_required(login_url="login")
def hompage(request):
    data = Content.objects.all().order_by('?')[:18]
    return render(request, 'index.html',{"data": data})


'''
    contents view checks whether the user is sending POST request or not;
    checks for the specific value that user have selected through dropdown and return context data
    filtering with that specific value
'''

@login_required(login_url="login")
def contents(request):
    if request.method == "POST":
        content = request.POST["dropdown"]
        data = Content.objects.filter(tag=content).order_by("-id")
        return render(request, 'content.html', {"data": data})


'''
    register_user view registers the new user
    request.user.is_authenticated ensures users are not already logged in such that no such user already exists
    After new user logins in, they are redirect to the login page
'''

def register_user(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                
                return redirect('login')
			

        context = {'form':form}
        return render(request, 'register.html', context)


'''
    login_user views ensures only authenticated user can enter to the website.
    request.user.is_authenticated redirects user to homepage if logged in user wants to login again
    authenticate(request, username=username, password=password) authenticates the user entered value with database value,
    if they matches then they are redirected to homepage, else error message is sent.
'''

def login_user(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, 'Username or password is incorrect')

        return render(request, 'login.html')


'''
    logout_user views simply logout the user and redirects to the login page
'''

def logout_user(request):
    logout(request)
    return redirect('login')                  
