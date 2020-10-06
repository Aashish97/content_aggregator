from django.conf import settings
from .models import Content
import re

# Importing requests and BeautifulSoup for the scraping of the content
import requests
from bs4 import BeautifulSoup

'''
    Beautiful soup is the library used for scraping the web contents in simple way
    doc variable stores all the html contents from the given link
    soup variable stores all the elements of the that doc variable
    html5lib is the parser which converts the html documents into the text format
    headers variable lists all the documents with matches the given condition
    The find_all method searches for all the tags and the class mentioned below
'''

# sites list all the sites for scrapping the content

sites = [
    "https://www.sharesansar.com/category/latest",
    "https://www.gsmarena.com/news.php3",
    "https://kathmandupost.com/sports",
    "https://kathmandupost.com/politics",
    "https://merojob.com/search/",
    ]

'''
    CronJob saves the data from the above listed site and saves the data to the database
    CronJob iterates every single site mentioned above

    try block checks if the data are scraped or not; if yes saves the data otherwise it moves to next loop
    Database instances are created and manipulated accordingly

    Content.objects.filter(tag="").filter(headline="") checks whether the headline already exists in database or not
        if there is some content then it doesn't saves the data which helps in unique content in database always
'''

def CronJob():
    for site in sites:
        if site == sites[0]:
            doc = requests.get(sites[0])
            soup = BeautifulSoup(doc.content, "html5lib")
            blocks = soup.find_all('div', {'class':'featured-news-list'})
            for block in blocks:
                try:
                    content = Content()
                    content.headline = block.findChildren()[5].text
                    content.image = block.findChildren()[2].get('src')
                    content.link = block.findChildren()[1].get('href')
                    content.tag = "Shares"
                    data = Content.objects.filter(tag="Shares").filter(headline=content.headline)
                    if len(data) == 0:
                        content.save()
                except:
                    print("duplicate headline")

        elif site == sites[1]:
            doc = requests.get(sites[1])
            soup = BeautifulSoup(doc.content, "html5lib")
            blocks = soup.find_all('div', {'class':'news-item'})
            for block in blocks:
                try:
                    content = Content()
                    content.headline = block.findChildren()[4].text
                    content.image = block.findChildren()[2].get('src')
                    content.link ="https://www.gsmarena.com/" + block.findChildren()[1].get('href')
                    content.tag = "Gadgets"
                    data = Content.objects.filter(tag="Gadgets").filter(headline=content.headline)
                    if len(data) == 0:
                        content.save()
                except:
                    print("duplicate headline")

        elif site == sites[2]:
            doc = requests.get(sites[2])
            soup = BeautifulSoup(doc.content, "html5lib")
            blocks = soup.find_all('article', {'class':'article-image'})[0:20]
            for block in blocks:
                try:
                    content = Content()
                    content.headline = block.findChildren()[5].text
                    image_src = block.findChildren()[3].get('data-src')
                    content.image = re.split('[=|&]', image_src)[1]
                    content.link ="https://kathmandupost.com" + block.findChildren()[2].get('href')
                    content.tag = "Sports"
                    data = Content.objects.filter(tag="Sports").filter(headline=content.headline)
                    if len(data) == 0:
                        content.save()
                except:
                    print("duplicate headline")

        elif site == sites[3]:
            doc = requests.get(sites[3])
            soup = BeautifulSoup(doc.content, "html5lib")
            blocks = soup.find_all('article', {'class':'article-image'})[0:20]
            for block in blocks:
                try:
                    content = Content()
                    content.headline = block.findChildren()[5].text
                    image_src = block.findChildren()[3].get('data-src')
                    content.image = re.split('[=|&]', image_src)[1]
                    content.link ="https://kathmandupost.com" + block.findChildren()[2].get('href')
                    content.tag = "Politics"
                    data = Content.objects.filter(tag="Politics").filter(headline=content.headline)
                    if len(data) == 0:
                        content.save()
                except:
                    print("duplicate headline")
        
        if site == sites[4]:
            doc = requests.get(sites[4])
            soup = BeautifulSoup(doc.content, "html5lib")
            blocks = soup.find_all('div', {'class':'hover-shadow'})
            for block in blocks:
                try:
                    content = Content()
                    content.headline = block.findChildren()[4].find('h1').text
                    organization = block.findChildren()[5].find('meta').get('content')
                    skills = block.findChildren()[28].text
                    content.image = "https://merojob.com" +  block.findChildren()[5].find('img').get('src')
                    content.link = "https://merojob.com" +   block.findChildren()[4].find('a').get('href')
                    raw_body = organization + " (" + skills + ")"
                    content.body = re.sub(' +', ' ', raw_body)
                    content.tag = "Jobs"
                    data = Content.objects.filter(tag="Jobs").filter(headline=content.headline)
                    if len(data) == 0:
                        content.save()
                except:
                    print("duplicate headline")

        