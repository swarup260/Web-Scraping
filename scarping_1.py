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


"""
##testing
data = soup(getLink("https://myanimelist.net/") ,'html.parser')
print(data.title)
"""
'''
BeautifulSoup parser
1.html.parser
2.lxml (faster)
3.lxml-xml
4.html5lib (Very slow /External Python dependency)
'''
##get all the links 
html_data = getLink("")
data = soup(html_data,'html.parser')
with open('links.txt' ,'w') as f:
    for link in data.find_all('a'):
        f.write("\n"+str(link.get('href')))
    f.close()
            