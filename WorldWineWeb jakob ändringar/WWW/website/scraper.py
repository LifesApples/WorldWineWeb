from math import prod
import os
import requests
import json
import urllib.request, urllib.error, urllib.parse
from db_connection import *

from urllib.parse import urlencode, urlunparse,urlparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from flask import Blueprint, render_template

scraper = Blueprint('scraper', __name__)

class scraper:

    def __init__(self):
        pass
    #query = "Absolut vodka"
    #url = urlunparse(("https", "www.bing.com", "images/search?q=", "", urlencode({"q": query}), ""))

    def searchPics(pname, producer, bottletype):
        seartext = pname+" "+producer+" "+bottletype
        print("Text: " + seartext)
        count = 4
        sear=seartext.strip()
        sear=sear.replace(' ','+')
        URL='https://bing.com/images/search?q=' + sear
            #+ '&safeSearch=' + adlt + '&count=' + count
        custom_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        req = Request(URL, headers={"User-Agent": custom_user_agent})
        page = urlopen(req)
        # Further code I've left unmodified
        soup = BeautifulSoup(page.read(),features="html.parser")
        #links = soup.findAll("jpg")

        ActualImages=[]# contains the link for Large original images, type of  image
        wow = soup.find_all('a',class_='iusc')
        for i in wow:
            try:
                print(eval(i['m'])['murl'])
                print()
                break
            except:
                pass
    

    searchPics("Sju komma tvaan" , "Ljus lager", " Starkare lager")
    
    """""
    for a in soup.find_all("a",{"class":"iusc"}):
        print(a)
        # mad = json.loads(a["mad"])
        # turl = mad["turl"]
        m = json.loads(a["m"])
        murl = m["murl"]
        turl = m["turl"]
        print("URL Should be: " + murl)

        image_name = urllib.parse.urlsplit(murl).path.split("/")[-1]
        print("Name is: " + image_name)

        ActualImages.append((image_name, turl, murl))

    print("there are total" , len(ActualImages),"images")
    """
    """"
    ------------------------------------------------------
    for link in links:
        print("Denna " + link["href"])

    """
    """
    from google_images_search import GoogleImagesSearch

    ##response = requests.get( , data = {'key':'AIzaSyBRZHKkHm_WpiMzQM4z6W-YEVKSedRv3Ck'})

    headers = {
        # Request headers

    }
    apiKey = "AIzaSyBRZHKkHm_WpiMzQM4z6W-YEVKSedRv3Ck"
    project = "34b8f4687e269165a"
    gis = GoogleImagesSearch(apiKey,project)
    test = requests.get("https://www.googleapis.com/customsearch/v1?key=AIzaSyBRZHKkHm_WpiMzQM4z6W-YEVKSedRv3Ck"
                        "&cx=017576662512468239146:omuauf_lfve&q=lectures,developerKey=key")


    _search_params = {
        'q'       : 'Persian Cat',
        'num'     : 10,
        'safe'    : 'high',
        'fileType': 'jpg|png',
        'imgType' : 'photo',
    }
    # search first, then download and resize afterwards:
    gis.search(search_params=_search_params,  custom_image_name='persian')

    for image in gis.results():
        image.download('/Users/azamsuleiman/Downloads/Katter') #download images to the directory
        image.resize(500, 500) # resize image

    os.listdir('/Users/azamsuleiman/Downloads/Katter')
    """