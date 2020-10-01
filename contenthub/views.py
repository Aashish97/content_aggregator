from django.shortcuts import render
import re
import random

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
    "https://kathmandupost.com/politics",
    "https://www.gsmarena.com/news.php3",
    "https://kathmandupost.com/sports",
    "https://merojob.com/search/",
    ]

home_data = []

def sharemarket(request):
    doc = requests.get(sites[0])
    soup = BeautifulSoup(doc.content, "html5lib")
    data = []
    blocks = soup.find_all('div', {'class':'featured-news-list'})
    for block in blocks:
        headline = block.findChildren()[5].text
        image = block.findChildren()[2].get('src')
        readmore = block.findChildren()[1].get('href')
        data.append([headline, image, readmore])
    home_data.append(data)
    return render(request, './../templates/contents.html', {"data": data})

def politics(request):
    doc = requests.get(sites[1])
    soup = BeautifulSoup(doc.content, "html5lib")
    data = []
    blocks = soup.find_all('article', {'class':'article-image'})
    for block in blocks:
        headline = block.findChildren()[5].text
        image_src = block.findChildren()[3].get('data-src')
        image = re.split('[=|&]', image_src)[1]
        readmore ="https://kathmandupost.com" + block.findChildren()[2].get('href')
        data.append([headline, image, readmore])
    home_data.append(data)
    return render(request, './../templates/contents.html', {"data": data})

def gadgets(request):
    doc = requests.get(sites[2])
    soup = BeautifulSoup(doc.content, "html5lib")
    data = []
    blocks = soup.find_all('div', {'class':'news-item'})
    for block in blocks:
        headline = block.findChildren()[4].text
        image = block.findChildren()[2].get('src')
        readmore ="https://www.gsmarena.com/" + block.findChildren()[1].get('href')
        data.append([headline, image, readmore])
    home_data.append(data)
    return render(request, './../templates/contents.html', {"data": data})

def sports(request):
    doc = requests.get(sites[3])
    soup = BeautifulSoup(doc.content, "html5lib")
    data = []
    blocks = soup.find_all('article', {'class':'article-image'})
    for block in blocks:
        headline = block.findChildren()[5].text
        image_src = block.findChildren()[3].get('data-src')
        image = re.split('[=|&]', image_src)[1]
        readmore ="https://kathmandupost.com" + block.findChildren()[2].get('href')
        data.append([headline, image, readmore])
    home_data.append(data)
    return render(request, './../templates/contents.html', {"data": data})

def jobs(request):
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
        data.append([headline, image, readmore, body])
    home_data.append(data)
    return render(request, './../templates/contents.html', {"data": data})

def hompage(request):
    return render(request, 'index.html',{"data": home_data})
