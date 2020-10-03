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

# Importing requests and BeautifulSoup for the scraping of the content
import requests
from bs4 import BeautifulSoup

'''
    doc variable stores all the html contents from the given link
    soup variable stores all the elements of the that doc variable
    html5lib is the parser which converts the html documents into the text format
    headers variable lists all the documents with matches the given condition
    The find_all method searches for all the tags and the class mentioned below
'''

@login_required(login_url="login")
def hompage(request):
    return render(request, 'index.html',{})

@login_required(login_url="login")
def contents(request):
    if request.method == "POST":
        content = request.POST["dropdown"]

        if content == "Sharemarket":
            data = Content.objects.filter(tag="Shares")
            return render(request, './../templates/content.html', {"data": data})

        elif content == "Gadgets":
            data = Content.objects.filter(tag="Gadgets")
            return render(request, './../templates/content.html', {"data": data})

        if content == "Sports":
            data = Content.objects.filter(tag="Sports")
            return render(request, './../templates/content.html', {"data": data})

        elif content == "Politics":
            data = Content.objects.filter(tag="Politics")
            return render(request, './../templates/content.html', {"data": data})

        else:
            data = Content.objects.filter(tag="Jobs")
            return render(request, './../templates/content.html', {"data": data})

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

def logout_user(request):
    logout(request)
    return redirect('login')                  
