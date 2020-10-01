from django.shortcuts import render
import re

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
    ]


def hompage(request):
    return render(request, 'index.html',{})

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
    return render(request, './../templates/contents.html', {"data": data})



