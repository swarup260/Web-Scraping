'''
    Web Scraping Class for Scraping
    the list of anime from myanimelist.net.
'''

#list of import packages
import requests as req
import json
import urllib.request
from bs4 import BeautifulSoup


# url : - https://myanimelist.net/anime/season/2018/summer


'''
  Scrap the data from myanimelist.net 
  all copyright reserved to myanimelist.ney
'''
class MyAnimeList(object):
    def __init__(self,yrs,season):
        self.baseUrl = "https://myanimelist.net"
        self.yrs = yrs
        self.season = season
        self.result = []
        self.url = self.baseUrl+"/anime/season/"+str(yrs)+"/"+season
        self.filename = str(self.yrs) + self.season + ".json"

    def load(self,url):
        try:
            self.urlData = req.get(url).text
            return self.urlData
        except:
            return "failed to retrive from url"

    def scrapingData(self):
        self.soup = BeautifulSoup(self.load(self.url), 'html.parser')
        self.imgTag = self.soup.find_all('div', attrs={'class': 'image'})
        self.desps = self.soup.find_all('span', attrs={'class': 'preline'})
        self.scores = self.soup.find_all('span', attrs={'class': 'score'})
        self.eps = self.soup.find_all('div', attrs={'class': 'eps'})
        self.scores = self.soup.find_all('span', attrs={'class': 'score'})
        self.animeTimes = self.soup.find_all('span', attrs={'class': 'remain-time'})

        for i in range(len(self.imgTag)):
            innerImg = self.imgTag[i].find_all('img')
            ep = self.eps[i].find_all('span')
            for src in innerImg:
                for eacheps in ep:
                    if str(src.get('src')) != 'None':
                        name = src.get('alt')
                        src = str(src.get('data-src'))
                    else:
                        name = src.get('alt')
                        src = str(src.get('data-src'))
                id = i
                episode = str(eacheps.text).strip()
                despcrition = self.desps[i].text
                Rating = self.scores[i].text
                time = str(self.animeTimes[i].text).strip()
                self.dict = {"id": id, "AnimeTitle": name, "Imgurl": src, "Despcrition": despcrition, "Rating": Rating,
                        "Datetime": time, "Episode": episode}
                self.result.append(self.dict)
        return self.result


    def jsonWriter(self,filename,data):
        try:
            with open(filename ,'w+') as outfile:
                json.dump(data, outfile)
                return "SuccessFully Write to json"
        except:
                return " Fail to writer to file"

    def topAnime(self,type):
        dictType = {"topAnime":"/topanime.php" ,
                "topAiring":"/topanime.php?type=airing" ,
                "topUpcoming":"/topanime.php?type=upcoming",
                "TopMovie" :"/topanime.php?type=movie",
                "TopTvSeries":"/topanime.php?type=tv",
                "TopOva": "/topanime.php?type=ova"
                }
        self.topurl = self.baseUrl+dictType[type]
        print(self.topurl)
        # exit()
        self.soup = BeautifulSoup(self.load(self.topurl), 'lxml')
        self.ranks = self.soup.find_all('span' ,attrs={'class':'top-anime-rank-text'})
        self.info  = self.soup.find_all('div',attrs={'class':'information'})
        self.imgTag = self.soup.find_all('img',attrs={"class":"lazyload"})

        for num in range(len(self.imgTag)):
            name = self.imgTag[num].get('alt')
            src = str(self.imgTag[num].get('data-src'))
            rank= str(self.ranks[num].text)
            info = self.info[num].text
            self.dict = {"rank":rank,"name": name, "imgUrl": src, "typeAiringDataTotalVote": info}
            self.result.append(self.dict)
        return self.jsonWriter(type+".json",self.result)

    def printurl(self):
        return  self.url


obj = MyAnimeList(yrs=2017,season="spring")
data = obj.scrapingData()
obj.jsonWriter("anime_data2017.json",data)