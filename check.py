from urllib2 import urlparse
import justext
import requests

def if_review(text):
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

#response = requests.get("https://www.tripadvisor.in/Hotels-g297685-oa30-Varanasi_Uttar_Pradesh-Hotels.html")
#paragraphs = justext.justext(response.content, justext.get_stoplist("English"))

#for para in paragraphs:
para = "05/01/2017 “Short stay in Royal Guest House”"
a,b = if_review(para)
if a>0:
		print para