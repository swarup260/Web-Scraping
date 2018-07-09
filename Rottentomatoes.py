from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
import json


'''
list of url : -
https://www.rottentomatoes.com/browse/opening/
https://www.rottentomatoes.com/browse/in-theaters/
https://www.rottentomatoes.com/browse/upcoming/


scraping tags :-

img :- class="poster" [img url and alt name ]
title :- <h3 class="movieTitle">Avengers: Infinity War</h3>
score :- <span class="tMeterScore">84%</span>
Date : - <p class="release-date">In Theaters Apr 27</p>
'''


class RottenTomatoes(object):
    def __init__(self,option):
        self.option = option
        self.url = "https://www.rottentomatoes.com/browse/"
        self.scrapingUrl = self.url+option
        self.result = []

    def printUrl(self):
        print(self.scrapingUrl)

    def scarpingData(self):
        browser = webdriver.Firefox(executable_path='C://driver//geckodriver')
        browser.get(self.scrapingUrl)
        time.sleep(5)
        movieFrame = browser.find_elements_by_xpath('.//*[@class="mb-movie"]')
        for frame in movieFrame:
            try:
                scrs = frame.find_elements_by_xpath('.//span[@class="tMeterScore"]')
                for num  in range(len(scrs)):
                    if (len(scrs) == 2):
                        rottenScore = scrs[0].text
                        popcornScore = scrs[1].text
                    elif(len(scrs) == 1):
                        rottenScore = scrs[0].text
                        popcornScore = "None"
            except Exception:
                rottenScore = "None"
                popcornScore = "None"
            img = frame.find_element_by_class_name('poster').get_attribute('src')
            title = frame.find_element_by_xpath('.//*[@class="movieTitle"]').text
            date = frame.find_element_by_xpath('.//*[@class="release-date"]').text
            dict = {"Title": title, "ImgUrl": img, "Rotten-Scores": rottenScore,"PopcornScore":popcornScore, "Date": date}
            self.result.append(dict)
        return self.result

    def jsonWriter(self,filename,data):
        try:
            with open(filename ,'w+') as outfile:
                json.dump(data, outfile)
                return "SuccessFully Write to json"
        except:
                return " Fail to writer to file"




obj = RottenTomatoes('in-theaters')
data = obj.scarpingData()
obj.jsonWriter('in-theatersRevised.json',data)


# url = "https://www.rottentomatoes.com/browse/opening"
# browser = webdriver.Firefox(executable_path='C://driver//geckodriver')
# browser.get(url)
# time.sleep(5)
# movieFrame = browser.find_elements_by_xpath('.//*[@class="mb-movie"]')
# for frame in movieFrame:
#     try:
#         scrs = frame.find_elements_by_xpath('.//*[@class="tMeterScore"]')
#         for src in scrs:
#             rottenScore = src.text
#
#     except Exception:
#         rottenScore = "None"






