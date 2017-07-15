from urllib2 import urlparse
import justext
import requests
from chat import *
class place2visit:
	def __init__(self,urll):
         self.url1=urll
		#	self.txt=text
	def place(self):
		#link = list()
		desc = dict()
		f=0
		myset=set()
		#link.append(l1)
		#link.append(l2)
		#link.append(l3)
		#link.append(l4)
		#link.append(l5)
		#ink.append(l6)
		st=""
		state=""
		a=["Amusement","Beach","hall","centre","Waterfall","Park","Temple","Zoo","Stadium","Church","Masjid","Museum","Mall","Sea","Club","Retreat","Garden","Mandir","valley","Ashram","Palace","Kila","Quila","Qila","Art","Gallery","Mahal","Minar","Fort","Jheel","Mandir","St.","Bridge","Mahal","Island","Santa","Tower","Casino","Market","Hall","Theatre","Market","River","Garden"]
		link=list()
		link.append(self.url1)
		for k in link:

			#response = requests.get("https://www.tripadvisor.in/Hotels-g667805-Kanpur_Uttar_Pradesh-Hotels.html")
			response = requests.get(k)
			#response = requests.get("https://www.ixigo.com/temples-in-kanpur-lp-1050363")
			#response = requests.get("https://www.goibibo.com/hotels/hotels-in-kanpur/")
			#response = requests.get("https://www.makemytrip.com/hotels-international/italy/rome-hotels/")#this we can achieve hotel name + address 

			paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
			for para in paragraphs:
				#

				st=para.text

				tag=len(st.split())
				word=st.split()
   		
				flg=0
				flag=0
				for i in a:
					if st.find(i)!=-1 and st.find(":")==-1:
						flag=1
						break
				for i in range(0,tag):
					#print word[i][0]
					if word[i][0].isupper():
						flg=flg+1
				if flag==1 and flg==tag:
					#print "all capitals"
					#print st
					flag=1
				elif flag==1 and flg==(tag-1) and st.find("of")!=-1:
					#print "of found"
					#print st
					flag=1
				else:
					flag=0
				sz=len(st)
				if st[sz-1]=='s':
					flag=0

				if  tag>1 and flag==1:#place 2 visit found
					r = st.find(',')
					if r!=-1:
						st = st[:r]
					myset.add(st)
					#print st
					state=st
					f=1
					desc[state] = "No desc"

		#key = desc.keys()
		for k in link:
			response = requests.get(k)
			paragraphs = justext.justext(response.content, justext.get_stoplist("English"))

			for para in paragraphs:
				newt = para.text
				vnewt = newt.lower()
				flg=0
				for item in myset:
					item=item.lower()
					if vnewt.find(item)!=-1:
						flg=flg+1
				for item in myset:
					nitem = item.lower()
					length = len(desc[item])
					word=newt.split()
					tag=len(newt.split())
   		
					if vnewt.find(nitem)!=-1:
						if tag> 10 and (desc[item] == "No desc" or length<len(newt)) and flg<=1 and vnewt.find("hotels near")==-1:
							desc[item] = newt


		aplc = list()
		bplc = list()
		ades = list()
		bdes = list()
		
		ajoobadict=dict()
		for item in myset:
			ajoobadict[item]=desc[item]
		return ajoobadict