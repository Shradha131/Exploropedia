from urllib2 import urlparse
import justext
import requests
api_key = 'AIzaSyAgrzXLdY810gb4BMXNYp1tMT4eJrB7934'
import sys
reload(sys)
from chat import *
sys.setdefaultencoding('utf8')

mydict = dict()
adrdict = dict()
revwc = dict()
revdict = dict()
ratedict = dict()

class newpro:
	
	def if_review(self,text):
		#print "egf"
		cnt = 0
		a = ["great","best","home","good","bad","pathetic","perfect","nice","hygiene","poor","stay","average","location","ok","comfort","staff","convenient","relax","hospitality","safety","cheap","favourite","amazing","fantastic","elegant","love","like","friendly"]
		mtext = text.lower()
		w=mtext.split()
		for i in a:
			for j in w:
				if i==j:
					cnt = cnt+1

		wc=len(mtext.split())
   	
		return cnt,wc

	def if_addr(self,add):
		cnt=0
		r=0
		flag = 0
		a=["/","-","near","Opp","behind","in front of","Rd","road","Road","market",",","Kanpur"]
		b = ["Reviews","reviews",":"]
		for i in b:
			if add.find(i)!=-1:
				flag = 1
		for i in a:
			cnt=cnt+add.count(i)
		if cnt>0 and flag==0:
			r=1

		return r,cnt

	def if_rating(self,rate):
		cnt=0
		flag=0
		a=["/5","/ 5","/10","/ 10","/7","/ 7"]
		for i in a:
			if rate.find(i)!=-1 and rate.find(",")==-1:
				return 1
		return 0
	


	def bekar(self):
	
			
		words = ["Hotels","Booking","Deal","List","Type","By","Search","Contact","In","Chains","With","Smoking"]
		a=["buy","eat","sleep","Hotel","place","temple","visit","Landmark","international","breakfast","parking","Wi-Fi","budget","location","stay","dinner","room","staff","price","occupancy","booking","near","travel","guest","lodge","resort"]
		myset=set()
		rev=""
		for k in link:
			response = requests.get(k)
			paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
			st=""
			para=st
			address=0
			rvw_flg=0
			for paragraph in paragraphs:
				if address==1:
					st=paragraph.text
					valid,count = self.if_addr(paragraph.text)
					if valid==1:
						if adrdict.has_key(hotelnaam):
							if mydict[hotelnaam]<count:
								mydict[hotelnaam]=count
								adrdict[hotelnaam]=paragraph.text
						else:
							mydict[hotelnaam]=count
							adrdict[hotelnaam]=paragraph.text
					else:
						mydict[hotelnaam] = 0;


				rvalid,rwc = self.if_review(paragraph.text)
				if rvalid > 0 and rvw_flg==1 and rwc <= 50:
					if revdict.has_key(hotelnaam):
						if revwc[hotelnaam]<rwc:
							revwc[hotelnaam]=rwc
							revdict[hotelnaam]=paragraph.text
					else:
						revwc[hotelnaam]=rwc
						revdict[hotelnaam]=paragraph.text

   			#revdict[paragraph.text]="No Review Available"
				drate = self.if_rating(paragraph.text)
				if drate==1 and rvw_flg==1:
				#print "nai aaye tum hmare pas :("
					if ratedict[hotelnaam]=="No rating":
						pos = paragraph.text.find("/7")
						if pos!=-1:
							st = paragraph.text[:pos]
							st += "/7"
							ratedict[hotelnaam] = st
						else:
							ratedict[hotelnaam] = paragraph.text
				address=0
				cnt=0
				for b in a:
					if b in paragraph.text:
						cnt=cnt+1
				word=(paragraph.text).split()
				tag=len((paragraph.text).split())

				flg=0
				flag=0
				for i in words:
					if i in paragraph.text:
						flag=1
						break
				for i in range(0,tag):
					if word[i][0].isupper():
						flg=flg+1
				if  tag>1 and ((paragraph.text).find("Hotel")!=-1 or (paragraph.text).find("Apartments")!=-1 or (paragraph.text).find("Lodge")!=-1 or (paragraph.text).find("Hostel")!=-1 or (paragraph.text).find("Resort")!=-1 or (paragraph.text).find("Villa")!=-1 ) and flg==tag and flag!=1:
					hotelnaam=paragraph.text
					myset.add(paragraph.text)
					address=1
					rvw_flg=1
					revwc[paragraph.text]=0
					ratedict[paragraph.text] = "No rating"
   		
		items = mydict.keys();
		for item in items:
			if mydict[item] == 0:
				myset.remove(item);


		for item in myset:
			if revwc[item]==0:
				revdict[item]= "NO Review"

		name=list()
		addr=list()
		revw=list()
		rate=list()
		for item in myset:
			name.append(item)
		item=adrdict.keys()
		for i in item:
			addr.append(adrdict[i])
		item=revdict.keys()
		for i in item:
			revw.append(revdict[i])	
		for i in item:
			rate.append(ratedict[i])	
		return name,addr,revw,rate


