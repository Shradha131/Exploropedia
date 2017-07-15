import signal
import sys
import urlparse
import argparse
import requests

from bs4 import BeautifulSoup
from collections import deque
from do import *

from ask1 import *
from review import *
from chat import *
from newpro import *
from place import *

chamatkardict=dict()
loldict=dict()
naho=["train","flight","airport","transportation"]		
kkk = ""
URLS = set()                # Unique set of all urls collected
VISITED_LINKS = set()       # For crawling a url only once
VERBOSE = False
class crawler:
	def __init__(self, que):
		if que:
			self.question = que
	def signal_handler(self,signal, frame):
		"""exit gracefully on keybord interrupt"""
		print "\n\n[Stopped]"
		print "Found: %d links \n" % len(URLS)

		for link in URLS:
			print link
		sys.exit(0)
		

	def crawl(self,url, max_depth,k):
		"""The main crawler function.

    Takes a url and max_depth as input parameters and returns a list of crawled
    urls. Urls beyond max_depth are not crawled, (default: 10).
    """
		host = urlparse.urlparse(url)[1]   # For crawling same host urls
		depth = 0                   # Set the root depth to 0

    # add url to the url traversal queue, thus making it our starting url
		dq = deque()
		dq.append((url, depth))
		print 'Fetching urls...'
		print 'Press [Ctrl-C] to stop crawling anytime'
		bhaukal=list()
		m=k.split()		
							#print m		
		city=m[2]
		while len(dq) != 0:
			# pop the the first url and crawl
			current_url, depth = dq.popleft()
			req1=do(current_url)
			
			if current_url.find("kanhashyam") != -1:
				continue
			
			adbhutdict=req1.kanjoos(city)
			
			#123
			'''temp_key=adbhutdict.keys()
			for bhaalu in temp_key:
				if not loldict.has_key(bhaalu):
					loldict[bhaalu]=1
					adbhutdict[bhaalu].append(current_url)'''
			
			
		#	adbhutdict=req1.kanjoos(city)
		#123
			bhaukal.append(adbhutdict)
			
			#print 'Dekh BC ---------------'
			print current_url
			#print 'Dekh liya --------------'
			
			if depth >= max_depth:
				break
			if VERBOSE:
				print ('Crawling %s' % current_url)
        #print 'phew', current_url, check_if_not_visited(current_url),
        #check_if_same_host(host, current_url)
			#print 'shitt'
			if (current_url not in VISITED_LINKS) and  host ==  urlparse.urlparse(current_url)[1]:
				#print 'fhfhd'
				try:
					VISITED_LINKS.add(current_url)
					#page_links = self.fetch_all_links(current_url)
					url_list = []
					#print 'bhak'
					try:
						r = requests.get(current_url)
						if r.status_code == 200:
							if VERBOSE:
								print ('Fetching in page links...')
							#print r.status_code
							content = r.content
							soup = BeautifulSoup(content, "lxml")
							tags = soup('a')
							flg=0
							for a in tags:
								href = a.get("href")
								if href is not None:
									new_url = urlparse.urljoin(current_url, href)
									for i in naho:
										if new_url.find(i)!=-1:
											flg=1
									if new_url not in url_list and (new_url.find("pg")!=-1 or new_url.find("page")!=-1 or new_url.find("-oa")!=-1) and new_url.find("jpg")==-1:
									#if new_url not in url_list and (new_url.find("pg")!=-1 or new_url.find("page")!=-1):
										url_list.append(urlparse.urldefrag(new_url)[0])
							

						elif r.status_code == 403:
							print "Error: 403 Forbidden url"
						elif r.status_code == 404:
							print "Error: 404 URL not found"
						else:
							print "Make sure you have everything correct."

					except requests.exceptions.ConnectionError, e:
						print "Oops! Connection Error. Try again"


					for link in url_list:
						if link not in URLS:
							# increase the depth of the link since it is found on an
							# internal page
							if VERBOSE: 
								print ('Adding %s' % link)
							dq.append((link, depth+1))
							print 'Wait Its  Link'
							print link
							URLS.add(link)

				except Exception, e:
					pass
			else:
				continue
            
		return bhaukal

	#if __name__ == '__main__':
	def garda(self):
		try:
			# handle SIGINT
			'''signal.signal(signal.SIGINT, signal_handler)

			parser = argparse.ArgumentParser(
				prog="crawler",
				description="A basic implementation of a web crawler written in python.",
				epilog="For more information see http://github.com/shashankgroovy/crawler")

			parser.add_argument("url", help="the url to crawl")
			parser.add_argument("-d", "--depth", type=int, default=10,
								help="set the max_depth for crawling")
			parser.add_argument('-v', '--verbose', action="store_true",
							help="Toggle verbose on (default is off)")

			args = parser.parse_args()

			VERBOSE = args.verbose'''
			#url = args.url
			print self.question		
			k=self.question
			request=chat(self.question)
			link= request.chatbox()
			print link
			depth = 2
			
			finaldict=dict()
			bhaukali_list=list()
			for url in link:
				bhaukali_list=self.crawl(url, depth,k)
				for jazz in bhaukali_list:
					key=jazz.keys()
					for kara in key:
						#123
						'''if not loldict.has_key(kara):
							jazz[kara].append('No Website Found')'''
					
						if not finaldict.has_key(kara): 
							finaldict[kara]=jazz[kara]
						else:
							if finaldict[kara][0]=="No address found" and jazz[kara][0]!="No address found":
								finaldict[kara][0]=jazz[kara][0]
								#may have to be removed
								finaldict[kara][3]=jazz[kara][3]
							if finaldict[kara][1]=="NO Review" and jazz[kara][1]!="NO Review":
								finaldict[kara][1]=jazz[kara][1]
								#may have to be removed
								finaldict[kara][3]=jazz[kara][3]
							if finaldict[kara][2]=="No rating" and jazz[kara][2]!="No rating":
								finaldict[kara][2]=jazz[kara][2]
								#may have to be removed
								finaldict[kara][3]=jazz[kara][3]
			print "\n----------------------------------------"
			print "Found: %d links \n" % len(URLS)
			for link in URLS:
				print link

		except KeyboardInterrupt:
			pass
		return finaldict
