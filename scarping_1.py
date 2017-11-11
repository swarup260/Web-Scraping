# -*- coding: utf-8 -*-
"""
Simple Web Scraping
it take links from the user and return htmldata
"""

from bs4 import BeautifulSoup as soup
import requests

def getLink(url):
    print("Downloading")
    try:
        html = requests.get(url)
        htmldata = html.text
    except:
        print("Error while.. ")
    return htmldata


data = soup(getLink("https://myanimelist.net/") ,'html.parser')
print(data.title)