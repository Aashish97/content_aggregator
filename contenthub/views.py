from django.shortcuts import render

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

doc = requests.get("https://www.sharesansar.com/category/latest")
soup = BeautifulSoup(doc.content,"html5lib")
headers = soup.find_all('h4', {'class':'featured-news-title'})

# news list is assigned empty so that all other news can be appended and can be displayed easily
news = []

# This appends all the header one by one to the news list in text format
for header in headers:
    news.append(header.text)

# Create your views here.
def hompage(request):
    return render(request, 'index.html',{"news":news})