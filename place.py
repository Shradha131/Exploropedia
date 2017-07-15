from urllib2 import urlparse
import justext
import requests
from chat import *
naho=["train","flight","airport","transportation","hotels near",":","@"]	
class place2visit:
	def __init__(self, urll,text):
			self.urlu = urll
			self.txt=text
	def place(self): 
		link=list()
		link.append(self.urlu)
		todo = list()
		desc = dict()
		f=0
		myset=set()
		st=""
		state=""
		a=["Amusement","Beach","hall","centre","Ghat","Santuary","Waterfall","Park","Temple","Zoo","Stadium","Church","Masjid","Museum","Mall","Sea","Club","Retreat","Garden","Mandir","valley","Ashram","Palace","Kila","Quila","Qila","Art","Gallery","Mahal","Minar","Fort","Jheel","Mandir","St.","Bridge","Mahal","Island","Santa","Tower","Casino","Market","Hall","Theatre","Market","River","Garden"]
		#words=[""]nst
		for k in link:

			#response = requests.get("https://www.tripadvisor.in/Hotels-g667805-Kanpur_Uttar_Pradesh-Hotels.html")
			print "kkkkkk"
			print k
			response = requests.get(k)
			#response = requests.get("https://www.ixigo.com/temples-in-kanpur-lp-1050363")
			#response = requests.get("https://www.goibibo.com/hotels/hotels-in-kanpur/")
			#response = requests.get("https://www.makemytrip.com/hotels-international/italy/rome-hotels/")#this we can achieve hotel name + address 

			paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
			for para in paragraphs:
				#

				st=para.text


				'''hi="[edit]"
	   			#print st
	   			if f==1 and st.find("Do[edit]")!=-1:
	   				f=2
	   				print "mil gaya"
	   			elif f==2:
	   				print "sahi"
	   				print st
	   				print hi
	   				if st.find(hi)==-1:
	   					sst = st.find("edit")
	   					st = st[:sst]
	   					todo.append(st)
	   					print "sssfsfsg"
	   					print st
	   					print f
	   				else:
	   					print "matched"
	   					f=1'''


				word=st.split()
				tag=len(word)
				
   		
				flg=0
				flag=0
				for i in a:
					if st.find(i)!=-1:
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
				if st[sz-1]=='s' or st.find(":")!=-1:
					flag=0
				if st.count(".")>1 or st.find("Photo")!=-1 or st.find("If")!=-1 or st.find("Popular")!=-1:
					fg = 1
				#if st==""
				#print "----------------------------------------place 2 visit---------------------------------------------------------------------------"
				if  tag>1 and flag==1:#place 2 visit found
					r = st.find(',')
					if r!=-1:
						st = st[:r]
					myset.add(st)
					#print st
					state=st
					f=1
					desc[state] = "No desc"
					#print desc[state]

		#key = desc.keys()
		for k in link:
			response = requests.get(k)
			paragraphs = justext.justext(response.content, justext.get_stoplist("English"))

			for para in paragraphs:
				newt = para.text
				vnewt = newt.lower()
				chk=0
				for k in naho:
					if vnewt.find(k)!=-1:
						chk+=1
				flg=0
				fg=0
				if vnewt.count(self.txt.lower())>5 or vnewt.count(',')>12:
					fg = 1
				#if vnewt.count(".")>1 or vnewt.find("photo")!=-1:
				#	fg = 1
				for item in myset:
					#item=item.lower()
					nitem = item.lower()
					if vnewt.find(nitem)!=-1:
						flg=flg+1
				for item in myset:	
					nitem = item.lower()
					
					length = len(desc[item])
					word=newt.split()
					tag=len(word)
   		
					if vnewt.find(nitem)!=-1:
						#if tag> 10 and (desc[item] == "No desc" or length<len(newt)) and flg==1 and chk==0 and fg==0:
						if tag> 10 and desc[item] == "No desc" and flg==1 and chk==0 and fg==0:
							desc[item] = newt

		
		ajoobadict=dict()
		for item in myset:
			ajoobadict[item]=desc[item]
		return ajoobadict