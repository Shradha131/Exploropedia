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

class review:
    print "what"
    def __init__(self, question):
        print "ques:"+question
        if question:
            self.search = question

    def google_response(self,api_key):
        try:
            var=self.search
        #    cx='013654424276126139747:15pewgl9rbi'
            urllib2.quote(var)
            print 'hello'
            urllib2.quote(api_key)
            url='https://maps.googleapis.com/maps/api/place/details/json?reference=' + var + '&key=' + api_key
            response = urllib2.urlopen(url)
            result = response.read()
            answer = json.loads(result)
            print answer
            web=answer[u'result']
            print "SatyaSatyaSatya"+web
            '''
            if web.has_key(u'international_phone_number'):
                fone=web[u'international_phone_number']
            else:
                fone='+502 345 2165'
            if web.has_key(u'vicinity'):
                vic=web[u'vicinity']
            else:
                vic='Landmark:130/325'
            if web.has_key(u'opening_hours'):
                opn=web[u'opening_hours']
                opn=opn[u'weekday_text']
            else:
                opn='24 hours open'
            print "satya:"+opn
            if web.has_key(u'vicinity'):
                vic=web[u'vicinity']
            else:
                vic=' '
            if web.has_key(u'website'):
                site=web[u'website']
            else:
                site='#'
            if web.has_key(u'website'):
                map1=web[u'url']
            else:
                map1='#'
            '''
            fone=''
            vic=''
            opn=''
            site=''
            map1=''
            #map=web[u'url']
            print 'SatyaSatyaSatyaSatyaSatyaSatyaSatyaSatyaSatyaSatyaSatyaSatya'
            nam = ''
            rev = ''
            #if web.has_key(u'reviews'):
            answer = web[u'reviews']
            print "dekho"+answer
            #print answer
            #k=answer[u'results'][u'photos']
            google_text = ''
            
            z=0
            for x in answer[0:3]:
                nam+=x[u'author_name']
                nam+='*'
                rev+=x[u'text']
                    
                rev+='*'
                #img+=x[u'profile_photo_url']
                #img+='*'
                print '#'
                z=z+1
            print site
            #print img
            anss = (nam,rev,site,map1,fone,vic,opn)

            return anss
        except TypeError, URLError:
            google_text = ''
        return google_text