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

#ImgScraper for adding picture links to database
class scraper:

    def __init__(self):
        pass
    #Function for searching for images using database values and updating database with links
    def searchpics(productname,bottletextshort,volume,categorylevel1):
        
        nonformatedtext = '%s %s %s %s' % (productname,volume,bottletextshort,categorylevel1)
        nonformatedtext = str(nonformatedtext).encode('utf-8') #Endcode to avoid the request from throwing errors for åäö 
        nonformatedtext = str(nonformatedtext).replace('b', '') #Remove the letter B that keeps showing upp in the list
        nonformatedtext = str(nonformatedtext).replace("'", '') #Remove quote from each element 

        #Build search query
        searchtext=nonformatedtext.strip()
        searchtext = str(searchtext)
        searchtext=searchtext.replace(' ','+')
        
        #Search and get results
        URL='https://bing.com/images/search?q=' + searchtext
            #+ '&safeSearch=' + adlt + '&count=' + count
        custom_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        req = Request(URL, headers={"User-Agent": custom_user_agent})
        page = urlopen(req)
        
        #Get results, loops through results and return first value that meets the criteria. Return as URL (for the image)
        soup = BeautifulSoup(page.read(),features="html.parser")
        wow = soup.find_all('a',class_='iusc')
        for i in wow:
            try:
                 url = eval(i['m'])['murl']
                 print(url)
                 return url
            except:
               pass

        
    #This loop gets the first product that does not have a URL and uses searchproduct() to find a matching image
    #This operation is done 500 times or until all URL fields have a value (a link)  
    count = 500 
    for i in range(count):
        #Get values from product table where url is empty
        cur = conn.cursor()
        insert_script = 'SET search_path = "WorldWineWeb", am4404, public; select productname,bottletextshort,volume,categorylevel1 from product where "url" is NULL;'
        cur.execute(insert_script)
        #Get returned records and convert results to a list
        records = cur.fetchone()
        text = list(records)
        text = str(text).split(",")
    
        #Loop through results to create a list within a list and formate text along the way
        for counter,i in enumerate(text):
            text[counter] = str(text[counter]).replace('[', '')# remove open bracket from each element
            text[counter] = str(text[counter]).replace(')', '')# remove parenthesis from each element
            text[counter] = str(text[counter]).replace("'", '')# remove singlequote from each element
            text[counter] = str(text[counter]).replace("]", '')# remove close bracket from each element
            #Store first value without removing å,ä,ö. Needed in order to query database later
            if(counter == 0):
                orgValue = text[0]
            text[counter] = str(text[counter]).replace("å", 'a')# remove å from each element
            text[counter] = str(text[counter]).replace("ä", 'a')# remove ä from each element
            text[counter] = str(text[counter]).replace("ö", 'o')# remove ö from each element
            text[counter] = str(text[counter]).replace("Å", 'a')# remove Å from each element
            text[counter] = str(text[counter]).replace("Ä", 'a')# remove Ä from each element
            text[counter] = str(text[counter]).replace("Ö", 'o')# remove Ö from each element
            #If a field contains None remove it
            if(text[counter] == None):
                    text[counter] = ""
    
        #Search for image using the above list, a url is returned. Use the unchanged value (that contains å,ä,ö) and
        #use it in the query for the database.
        urlToSend = searchpics(text[0],text[1],text[2], text[3])   
        query = "SET search_path = 'WorldWineWeb', am4404, public; select updateurl('%s','%s');" % (orgValue,urlToSend)
        
        #Used for checking if update was made to the database   
        try:
            cur.execute(query)
            conn.commit()
            result = cur.rowcount
            for rows in cur:
                print("result after commit: ", rows)
        except Exception as error:
            print("Error: ", error)
