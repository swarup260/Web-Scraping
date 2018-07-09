'''

https://www.imdb.com/movies-coming-soon/2018-06/?ref_=cs_dt_pv
'''

from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
import json


class Imdb(object):
    pass




url ="https://www.imdb.com/chart/boxoffice?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=740b2354-425b-4cd3-947b-7f9cb4349875&pf_rd_r=DXCWK4Y89BB5YME311R1&pf_rd_s=right-7&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_cht_hd"
urldata = requests.get(url).text
soup = BeautifulSoup(urldata,'lxml')
# print(soup.prettify())



titles = soup.find_all('td',attrs={"class":'titleColumn'})
rating = soup.find_all('td',attrs={"class":'ratingColumn'})
gross = soup.find_all('td',attrs={"class":'secondaryInfo'})
totalWeek = soup.find_all('td',attrs={"class":'weeksColumn'})

for num in range((len(titles))):
    for title in titles:
        link = title.find_all('a')
        for href in link:
            urlTitle = "https://www.imdb.com"+href.get('href')
            EachData = requests.get(urlTitle).text
            soup2 = BeautifulSoup(EachData,'lxml')
            print(soup.find_all('h1'))