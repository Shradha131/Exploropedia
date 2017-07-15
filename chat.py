#import urllib2
#import json
#import random
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from ask import *



api_key = 'AIzaSyAgrzXLdY810gb4BMXNYp1tMT4eJrB7934' #Enter your Google Developer API here.
#api_key = 'AIzaSyDvEFBOh1gX49HLuUWBSR_1QJYSGvKxaBY' 

#User interface
class chat:
    def __init__(self, question):
        if question:
            self.search_query = question
    print "Chat with Mr. Brainy. Type exit to end."
    def chatbox(self):
		query = ''
		query = self.search_query.lower()
		request = Ask(query)
		text = request.google_response(api_key,num=10)
		#print text
		return text
		