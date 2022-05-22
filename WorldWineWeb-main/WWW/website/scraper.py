from math import prod
import os
import re
from this import d
import requests
import json
import urllib.request, urllib.error, urllib.parse

from db_connection import *

from urllib.parse import urlencode, urlunparse,urlparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from flask import Blueprint, render_template

scraper = Blueprint('scraper', __name__)

#ImgScraper klass för att lägga till bilder i databasen
class scraper:

    def __init__(self):
        pass
    #Funktion som söker efter bilder och uppdaterar databasen med URL till sökreusltatet/bilden.
    def searchpics(productname,bottletextshort,volume,categorylevel1):
        
        #Formaterar och tar bort extra tecken från texten som kommer från funktionens parametrar
        nonformatedtext = '%s %s %s %s' % (productname,volume,bottletextshort,categorylevel1)
        nonformatedtext = str(nonformatedtext).encode('utf-8') #Formaterar kod så att å,ä,ö blir läsbart. 
        nonformatedtext = str(nonformatedtext).replace('b', '') #Tar bort värdet b som kommer med i hämtningen
        nonformatedtext = str(nonformatedtext).replace("'", '') #Tar bort citattecken
        searchtext=nonformatedtext.strip() 
        searchtext = str(searchtext)
        searchtext=searchtext.replace(' ','+')
        
        #Bygger en söksträng som sedan används i sökningen
        URL='https://bing.com/images/search?q=' + searchtext
            #+ '&safeSearch=' + adlt + '&count=' + count
        custom_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        req = Request(URL, headers={"User-Agent": custom_user_agent})
        page = urlopen(req)
        
        #Hämta sökresultat och hämta första som är en bild länk
        soup = BeautifulSoup(page.read(),features="html.parser")
        wow = soup.find_all('a',class_='iusc')
        for i in wow:
            try:
                 url = eval(i['m'])['murl']
                 print(url)
                 return url
            except:
               pass

    
    #Loopar 500 gånger eller tills alla url fält har ett värde (en url). 
    count = 500 
    for i in range(count):
        #Hämtar en rad från product tabellen där url är tomt
        cur = conn.cursor()
        insert_script = 'SET search_path = "WorldWineWeb", am4404, public; select productname,bottletextshort,volume,categorylevel1 from product where "url" is NULL;'
        cur.execute(insert_script)
        #Hämtar raden, delar upp den och lägger i en lista
        records = cur.fetchone()
        text = list(records)
        text = str(text).split(",")
    
        #Loopar igenom listan och formaterar texten.
        for counter,i in enumerate(text):
            #Formaterar text för varje rad
            text[counter] = str(text[counter]).replace('[', '')
            text[counter] = str(text[counter]).replace(')', '')
            text[counter] = str(text[counter]).replace("'", '')
            text[counter] = str(text[counter]).replace("]", '')
            #Spara första värdet (produktnamnet) så att inte å,ä,ö tas bort. Behövs senare för att bygga strängen till databasen
            if(counter == 0):
                orgValue = text[0]
            #Ta bort å,ä,ö för varje element i listan.
            text[counter] = str(text[counter]).replace("å", 'a')# remove å from each element
            text[counter] = str(text[counter]).replace("ä", 'a')# remove ä from each element
            text[counter] = str(text[counter]).replace("ö", 'o')# remove ö from each element
            text[counter] = str(text[counter]).replace("Å", 'a')# remove Å from each element
            text[counter] = str(text[counter]).replace("Ä", 'a')# remove Ä from each element
            text[counter] = str(text[counter]).replace("Ö", 'o')# remove Ö from each element
            #Töm fältet om den innehåller None
            if(text[counter] == None):
                    text[counter] = ""
    
        #Söker efter en bild med värden från ovan lista. En url till bilden returneras.
        #Uppdatera sedan databasen med ny länk genom att kalla på funktionen updateurl()
        urlToSend = searchpics(text[0],text[1],text[2], text[3])   
        query = "SET search_path = 'WorldWineWeb', am4404, public; select updateurl('%s','%s');" % (orgValue,urlToSend)
        
        #Används för att kolla på vad databasen svarar
        try:
            cur.execute(query)
            conn.commit()
            result = cur.rowcount
            for rows in cur:
                print("result after commit: ", rows)
        except Exception as error:
            print("Error: ", error)
