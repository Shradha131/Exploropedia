#####
# Overview: This file implements a rudimentary chatbot that utilizes Twitter and Google search results to provide the answers.
# The program makes a call to Google's servers, retrieves the urls associated with the question and filters their HTML files
# for text. The text is then analyzed using a 3-gram. The most occuring phrase is returned.
# Written by Dmitri Skjorshammer.
#####

import urllib, urllib2, requests
import json
import logging
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
import pprint

# Class: Search
# Purpose: Makes a search object corresponding to a question the user asks.
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Ask:
    def __init__(self, question):
        if question:
            self.search_query = question
    def google_response(self,api_key,**kwargs):
        print "hey"
        try:
            q='+'.join(self.search_query.split())
            cx='013654424276126139747:15pewgl9rbi'
            urllib2.quote(q)
            urllib2.quote(cx)
            urllib2.quote(api_key)

            url='https://www.googleapis.com/customsearch/v1?q='+q+'&cx='+cx+'&key='+api_key
            results = json.loads(urllib2.urlopen(urllib2.Request(url)).read())
            results = results[u'items']# Filter out unecessary data.
            google_text = ''
            #text = ''
            i=0
            links=list()
            urls=["trivago","tripadvisor","goibibo","cleartrip","makemytrip"]
            for el in results[0:10]:
                url = el[u'link']
             #   for i in urls:
                #    if url.find(i)!=-1:
                links.append(url)
            #print links
        except TypeError, URLError:
            google_text = ''
        return links