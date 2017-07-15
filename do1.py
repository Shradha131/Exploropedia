from urllib2 import urlparse
import justext
import requests

mydict = dict()
adrdict = dict()
revwc = dict()
revdict = dict()
class do:
def if_review(text):
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

def if_addr(add):
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

words = ["Hotels","Booking","Deal","List","Type","By","Search","Contact","In","Chains","With","Smoking"]
a=["buy","eat","sleep","Hotel","place","temple","visit","Landmark","international","breakfast","parking","Wi-Fi","budget","location","stay","dinner","room","staff","price","occupancy","booking","near","travel","guest","lodge","resort"]
l1="https://www.tripadvisor.in/Hotels-g667805-Kanpur_Uttar_Pradesh-Hotels.html"
l2="https://www.ixigo.com/hotels-in-kanpur-lp-1050363?view=list&filterKeys=&filterValues=&sort=po&type=&order=dsc&adults=1&children=0&rooms=1&checkInDate=06042017&checkOutDate=08042017&city=Kanpur,%20india&cityId=1070252&metaSearch=true"
l3="https://www.ixigo.com/temples-in-kanpur-lp-1050363"
l4="https://www.goibibo.com/hotels/hotels-in-kanpur/"
l5="https://www.tripadvisor.in/Hotels-g1722390-Cape_Town_Western_Cape-Hotels.html"
#l5="https://www.goibibo.com/hotels/united-kingdom/hotels-in-london/"
link = list()
myset=set()
link.append(l1)
link.append(l2)
link.append(l3)
link.append(l4)
link.append(l5)
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
   			st=paragraph.text
   			valid,count = if_addr(paragraph.text)
   			if valid==1:
   				if adrdict.has_key(hotelnaam):
   					if mydict[hotelnaam]<count:
   						 mydict[hotelnaam]=count
   						 adrdict[hotelnaam]=paragraph.text
   				else:
   					mydict[hotelnaam]=count
   					adrdict[hotelnaam]=paragraph.text

   				print paragraph.text
				print "its valid n count is-------------------------------------------------"
				print count 

			else:
				mydict[hotelnaam] = 0;
				print paragraph.text
				print "----------------------------------------------------its NOT valid n count is-------------------------------------------------"

		rvalid,rwc = if_review(paragraph.text)
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
   		if  tag>1 and ((paragraph.text).find("Hotel")!=-1 or (paragraph.text).find("Apartments")!=-1 or (paragraph.text).find("Lodge")!=-1 or (paragraph.text).find("Hostel")!=-1 or (paragraph.text).find("Resort")!=-1 or (paragraph.text).find("Villa")!=-1 ) and flg==tag and flag!=1:
   		#print tag
   		#print word[0][0]
   			hotelnaam=paragraph.text
   			print paragraph.text
   			myset.add(paragraph.text)
   			address=1
   			rvw_flg=1
   			revwc[paragraph.text]=0
   			#rev = hotelnaamka
   #if cnt>=1:
   	#  print paragraph.text
   	# para+=paragraph.text
#print para
#print revwc["Hotel Ashoka"]
	#print "hm last h:"
	#print hotelnaam
	#revdict[hotelnaam]="NO REVIEW"
print "-----------------------------------now,i am printing set-----------------------------------------------------------------------------:"
print revwc["Hotel Mangalam"]
items = mydict.keys();
for item in items:
	if mydict[item] == 0:
		myset.remove(item);
print "myset:"

for item in myset:
	print item

print "revwc"
for item in revwc.keys():
	print item

for item in myset:
	if revwc[item]==0:
		revdict[item]= "NO Review"

print "om mangalam:"
#print revwc["Hotel Ashoka"]
for item in myset:
	print item
	print "address"
	print adrdict[item]
	print "review"
	print revdict[item]
#print if_review("Hotel Ashoka")
name=list()
addr=list()
revw=list()
for item in myset:
	name.append(item)
item=adrdict.keys()
for i in item:
	addr.append(adrdict[i])
item=revdict.keys()
for i in item:
	revw.append(revdict[i])	
print "final result:"
print name
print addr
print revw