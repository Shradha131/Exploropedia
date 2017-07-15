from urllib2 import urlparse
import justext
import requests


words = ["Brand","Class","Properties","Details","Lodges","Website","Hotels","Booking","Deal","List","Type","By","Top","More",",","..","Search","Contact","In","Chains","With","Smoking","Guide",":","Explore","Manage","Amenities","About","Policy","See","See All","Offer","Luxury","Policies","Register","Catering","Awards","Photos","Best"]
a=["buy","eat","sleep","Hotel","place","temple","visit","Landmark","international","breakfast","parking","Wi-Fi","budget","location","stay","dinner","room","staff","price","occupancy","booking","near","travel","guest","lodge","resort"]
#l1="https://www.expedia.co.in/Ho-Chi-Minh-City-Hotels.d178262.Travel-Guide-Hotels"
#l5="https://www.goibibo.com/hotels/united-kingdom/hotels-in-london/"
#link = list()	
#myset=set()
'''link.append(self.url1)
rev=""'''

class do:
	def __init__(self,urll):
		self.url1=urll
	def if_review(self,text):
	#print "egf"
		cnt = 0
		a = ["great","best","home","good","bad","pathetic","perfect","nice","hygiene","poor","stay","average","location","ok","comfort","staff","convenient","relax","hospitality","well","safety","cheap","favourite","amazing","fantastic","elegant","love","like","friendly"]
		mtext = text.lower()
		w=mtext.split()
		for i in a:
			for j in w:
				if i==j:
					cnt = cnt+1

		wc=len(mtext.split())

		if mtext.find("#")!=-1 or mtext.find("ticket")!=-1 or mtext.find("hotels")!=-1:
			cnt = 0
   	
		return cnt,wc


	def if_addr(self,add,sh):
		add = add.lower()
		cnt=0
		r=0
		flag = 0
		a=["/","-","near","opp","behind","in front of","road","market",","]
		b = ["reviews",":"]
		for i in b:
			if add.find(i)!=-1:
				flag = 1
		for i in a:
			if add.find(i)!=-1:
				cnt=cnt+1
		#if add.find(sh.lower())!=-1:
		#	cnt += 1
		if cnt>0 and flag==0:
			r=1
		adl = add.split()
		adll = len(adl)
		if add.find("#")!=-1 or add.find("|")!=-1 or adll>10:
			r=0
		return r,cnt

	def if_rating(self,rate):
		cnt=0
		flag=0
		a=["/5","/ 5","/10","/ 10","/7","/ 7"]
		if rate.count('/')>1:
			return 0
		for i in a:
			if rate.find(i)!=-1 and rate.find(",")==-1:
					return 1
		return 0

	def kanjoos(self,sheher):
		'''words = ["Hotels","Booking","Deal","List","Type","By","Search","Contact","In","Chains","With","Smoking","Explore","Guide",":","About"]
		a=["buy","eat","sleep","Hotel","place","temple","visit","Landmark","international","breakfast","parking","Wi-Fi","budget","location","stay","dinner","room","staff","price","occupancy","booking","near","travel","guest","lodge","resort"]
		#l1="https://www.expedia.co.in/Ho-Chi-Minh-City-Hotels.d178262.Travel-Guide-Hotels"
		#l5="https://www.goibibo.com/hotels/united-kingdom/hotels-in-london/"'''
		self.cete = sheher
		link = list()	
		myset=set()
		
		mydict = dict()
		adrdict = dict()
		revwc = dict()
		revdict = dict()
		ratedict = dict()
		
		link.append(self.url1)
		rev=""
		for k in link:

		#response = requests.get("https://www.tripadvisor.in/Hotels-g667805-Kanpur_Uttar_Pradesh-Hotels.html")
			response = requests.get(k)
	#response = requests.get("https://www.ixigo.com/temples-in-kanpur-lp-1050363")
	#response = requests.get("https://www.goibibo.com/hotels/hotels-in-kanpur/")
	#response = requests.get("https://www.makemytrip.com/hotels-international/italy/rome-hotels/")#this we can achieve hotel name + address 

			paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
			st=""
			para=st
			address=0
			rvw_flg=0
	
			for paragraph in paragraphs:
				if address==1:
					mydict[hotelnaam] = 0;
					st=paragraph.text
					valid,count =self.if_addr(paragraph.text,self.cete)
					if	valid==1:
						if adrdict.has_key(hotelnaam):
							if mydict[hotelnaam]<count:
								mydict[hotelnaam]=count
								adrdict[hotelnaam]=paragraph.text
						else:
							mydict[hotelnaam]=count
							adrdict[hotelnaam]=paragraph.text

					#	print paragraph.text
					#print "its valid n count is-------------------------------------------------"
					#	print count 

					#else:
						#mydict[hotelnaam] = 0;
				#	print paragraph.text
				#print "----------------------------------------------------its NOT valid n count is-------------------------------------------------"

				rvalid,rwc =self.if_review(paragraph.text)
				if rvalid > 0 and rvw_flg==1 and rwc <= 50:
					#print "nai aaye tum hmare pas :("
					if revdict.has_key(hotelnaam):
						if revwc[hotelnaam]<rwc:
							revwc[hotelnaam]=rwc
							revdict[hotelnaam]=paragraph.text
						#print hotelnaam
						#print paragraph.text
					else:
						revwc[hotelnaam]=rwc
						revdict[hotelnaam]=paragraph.text

				#revdict[paragraph.text]="No Review Available"
				drate =self.if_rating(paragraph.text)
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
   		#print "count relevance:"
   		#print paragraph.text
   		#print paragraph.cfclass
   		#print cnt
   		#print "counting words"
   		#print paragraph.text.word_count
				word=(paragraph.text).split()
				tag=len((paragraph.text).split())
   		#print "para hu mai"
   		#print paragraph.text
   
   		#print "num of words:"
   		#print tag
   		#print (paragraph.text).find("Hotel")
				flg=0
				flag=0
				for i in words:
					if i in paragraph.text:
						flag=1
						break
				for i in range(0,tag):
					#print word[i][0]
					if word[i][0].isupper():
						flg=flg+1
				if  tag>1 and ((paragraph.text).find("Hotel")!=-1 or (paragraph.text).find("Parador")!=-1 or (paragraph.text).find("Apartments")!=-1 or (paragraph.text).find("Lodge")!=-1 or (paragraph.text).find("Hostel")!=-1 or (paragraph.text).find("Resort")!=-1 or (paragraph.text).find("Villa")!=-1 ) and flg==tag and flag!=1:
   		#print tag
   		#print word[0][0]
					hotelnaam=paragraph.text
				#	print "yhi hai"
				#	print paragraph.text
					myset.add(paragraph.text)
					address=1
					rvw_flg=1
					revwc[paragraph.text]=0
					ratedict[paragraph.text] = "No rating"
   			#rev = hotelnaamka
   #if cnt>=1:
   	#  print paragraph.text
   	# para+=paragraph.text
#print para
#print revwc["Hotel Ashoka"]
	#print "hm last h:"
	#print hotelnaam
	#revdict[hotelnaam]="NO REVIEW"
#print "-----------------------------------now,i am printing set-----------------------------------------------------------------------------:"
#print revwc["Hotel Mangalam"]
		#items = mydict.keys();
		for item in myset:
			if mydict[item] == 0:
				adrdict[item]="No address found"
#print "myset:"

#for item in myset:
	#print item

#print "revwc"
#for item in revwc.keys():
	#print item

		for item in myset:
			if revwc[item]==0:
				revdict[item]= "NO Review"

#print "om mangalam:"
#print revwc["Hotel Ashoka"]
#for item in myset:
	#print item
#	print "address"
	#print adrdict[item]
	#print "review"
	#print revdict[item]
	#print "rating"
	#print ratedict[item]
#print if_review("Hotel Ashoka")
		name=list()
		addr=list()
		revw=list()
		naam=""
		add=""
		rvw=""
		for item in myset:
			name.append(item)
			naam=naam+item+'#'
	#	print 'bhaaaaaaaaaaaak'
	#	print naam
		item=adrdict.keys()
		for i in item:
			addr.append(adrdict[i])
			add=add+adrdict[i]+'@'
		item=revdict.keys()
		for i in item:
			revw.append(revdict[i])
			rvw=rvw+revdict[i]+'$'
	#	print "final result:"
		#print name
		#print  'kutta'
		#print naam
	#	ajooba=list()
		ajoobadict=dict()
		for i in item:
			ajooba=list()
			ajooba.append(adrdict[i])
			ajooba.append(revdict[i])
			ajooba.append(ratedict[i])
			#123
			ajooba.append(k)
			ajoobadict[i]=ajooba
		return ajoobadict
#print addr
#print revw