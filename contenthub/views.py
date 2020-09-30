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
        data.append([headline, image])
    return render(request, 'sharemarket.html', {"data": data})

def politics(request):
    images= []
    headlines=[]
    doc = requests.get(sites[1])
    soup = BeautifulSoup(doc.content, "html5lib")
    headers = soup.find_all('h3')
    image_links = soup.find_all('img',{'class':'lazy img-responsive'})
    for image in image_links:
        image_src = str(image.get('data-src'))
        clean_image = re.split('[=|&]', image_src)
        print("clean image url >>>", clean_image)
        # if (clean_image[1] == 0):
        #     print("first image>>>", image_src)
        #     images.append(image_src)
        # else:
        #     print("second image>>>", clean_image[1])
        #     images.append(clean_image)
    for header in headers:
        headlines.append(header.text)
    return render(request, 'politics.html',{"headlines":headlines, "images": images})


