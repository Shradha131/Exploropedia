#####
# Overview: This file implements a rudimentary chatbot that utilizes Twitter and Google search results to provide the answers.
# The program makes a call to Google's servers, retrieves the urls associated with the question and filters their HTML files
# for text. The text is then analyzed using a 3-gram. The most occuring phrase is returned.
# Written by Dmitri Skjorshammer.
#####

import urllib, urllib2, requests
import json
import logging
from googleapiclient.discovery import build
import pprint


# Class: Search
# Purpose: Makes a search object corresponding to a question the user asks.
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Ask1:
    print "what"
    def __init__(self, question):
    	print "ask k ques:"+question
    	if question:
    		self.search_query = question

    def google_response(self,api_key):
        try:
            q='+'.join(self.search_query.split())
        #    cx='013654424276126139747:15pewgl9rbi'
            urllib2.quote(q)
            print 'hey'
            urllib2.quote(api_key)
            url='https://maps.googleapis.com/maps/api/place/textsearch/json?query='+q+'&key='+api_key
            response = urllib2.urlopen(url)
            result = response.read()
            answer = json.loads(result)
            answer = answer[u'results']
            #print answer
            #k=answer[u'results'][u'photos']
            google_text = ''
            nam = ''
            add = ''
            img = ''
            ref = ''
            z=0
            
            k=len(answer)
            print "Length ask.py mein : "
            print k
            l=7
            if k<7:
                l=k
            for x in answer[0:l]:
                add+= x[u'formatted_address']
                add+='#'
                if x.has_key(u'name'):
                    nam+= x[u'name']
                else:
                	nam+='SAtya'
                #nam+='<br />'
                nam+='$'
                #if x.has_key(u'photos'):
                if x.has_key(u'photos'):
                    img+=x[u'photos'][0][u'photo_reference']
                else:
                    img+='yo'
                img+='@'
                if x.has_key(u'reference'):
                    ref+=x[u'reference']
                else:
                    ref+='CmRSAAAAgppN3EwnNi1Pfi19SZ_AuH8XTX7U5jxZUxhPxaBAYIFtX8zpVcx8FJuI6kfKo3j-qmBO5NirAF9Iia7LSuah5_o-tHEBWqcQKfEl6aa8WluRQp8JuwANtcxO-KHL7UBhEhDgdb1ktGzC4b0qom8MLYfCGhTn0a6Diysipd0UNc6PLwS8KsSvrA'
                ref+='*'
                print '#'
                z=z+1
            bola=1
            print 'abey yaar'
            for xx in range(l,7):
                print bola
                bola=bola+1
            	nam+='No result to display'
            	nam+='$'
                add+='No result to display'
                add+='#'
            	img+='yo'
            	img+='@'
            	ref+='CmRSAAAAgppN3EwnNi1Pfi19SZ_AuH8XTX7U5jxZUxhPxaBAYIFtX8zpVcx8FJuI6kfKo3j-qmBO5NirAF9Iia7LSuah5_o-tHEBWqcQKfEl6aa8WluRQp8JuwANtcxO-KHL7UBhEhDgdb1ktGzC4b0qom8MLYfCGhTn0a6Diysipd0UNc6PLwS8KsSvrA'
            	ref+='*'
        #    print img
            anss = (nam,add,img,ref)

            return anss
        except TypeError, URLError:
            google_text = ''
        return google_text