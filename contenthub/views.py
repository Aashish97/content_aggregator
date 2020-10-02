from django.shortcuts import render, redirect
from django.http import JsonResponse
import re

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

sites = [
    "https://www.sharesansar.com/category/latest",
    "https://www.gsmarena.com/news.php3",
    "https://kathmandupost.com/sports",
    "https://kathmandupost.com/politics",
    "https://merojob.com/search/",
    ]

@login_required(login_url="login")
def hompage(request):
    return render(request, 'index.html',{})

@login_required(login_url="login")
def contents(request):
    if request.method == "POST":
        content = request.POST["dropdown"]

        if content == "Sharemarket":
            doc = requests.get(sites[0])
            soup = BeautifulSoup(doc.content, "html5lib")
            data = []
            blocks = soup.find_all('div', {'class':'featured-news-list'})
            for block in blocks:
                headline = block.findChildren()[5].text
                image = block.findChildren()[2].get('src')
                readmore = block.findChildren()[1].get('href')
                # dictionary for api related stuffs
                news = {
                    "headline": headline,
                    "image": image,
                    "link": readmore
                }
                """
                for json output
                    return JsonResponse(data)
                """
                data.append(news)
            return render(request, './../templates/content.html', {"data": data, "content": content })

        elif content == "Gadgets":
            doc = requests.get(sites[1])
            soup = BeautifulSoup(doc.content, "html5lib")
            data = []
            blocks = soup.find_all('div', {'class':'news-item'})
            for block in blocks:
                headline = block.findChildren()[4].text
                image = block.findChildren()[2].get('src')
                readmore ="https://www.gsmarena.com/" + block.findChildren()[1].get('href')

                # dictionary for api related stuffs
                news = {
                    "headline": headline,
                    "image": image,
                    "link": readmore
                }
                data.append(news)
            return render(request, './../templates/content.html', {"data": data, "content": content })

        if content == "Sports":
            doc = requests.get(sites[2])
            soup = BeautifulSoup(doc.content, "html5lib")
            data = []
            blocks = soup.find_all('article', {'class':'article-image'})
            for block in blocks:
                headline = block.findChildren()[5].text
                image_src = block.findChildren()[3].get('data-src')
                image = re.split('[=|&]', image_src)[1]
                readmore ="https://kathmandupost.com" + block.findChildren()[2].get('href')

                # dictionary for api related stuffs
                news = {
                    "headline": headline,
                    "image": image,
                    "link": readmore
                }
                data.append(news)
            return render(request, './../templates/content.html', {"data": data, "content": content })

        elif content == "Politics":
            doc = requests.get(sites[3])
            soup = BeautifulSoup(doc.content, "html5lib")
            data = []
            blocks = soup.find_all('article', {'class':'article-image'})
            for block in blocks:
                headline = block.findChildren()[5].text
                image_src = block.findChildren()[3].get('data-src')
                image = re.split('[=|&]', image_src)[1]
                readmore ="https://kathmandupost.com" + block.findChildren()[2].get('href')

                # dictionary for api related stuffs
                news = {
                    "headline": headline,
                    "image": image,
                    "link": readmore
                }
                data.append(news)
            return render(request, './../templates/content.html', {"data": data, "content": content })

        else:
            doc = requests.get(sites[4])
            soup = BeautifulSoup(doc.content, "html5lib")
            data = []
            blocks = soup.find_all('div', {'class':'hover-shadow'})
            for block in blocks:
                readmore ="https://merojob.com" +   block.findChildren()[4].find('a').get('href')
                headline = block.findChildren()[4].find('h1').text
                organization = block.findChildren()[5].find('meta').get('content')
                skills = block.findChildren()[28].text
                image ="https://merojob.com" +  block.findChildren()[5].find('img').get('src')
                raw_body = organization + " (" + skills + ")"
                body = re.sub(' +', ' ', raw_body)

                # dictionary for api related stuffs
                news = {
                    "headline": headline,
                    "image": image,
                    "link": readmore
                }
                data.append(news)
            """
            for json output
                return JsonResponse(data)
            """
            return render(request, './../templates/content.html', {"data": data, "content": content })

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
