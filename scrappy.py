
#from 'bhakk.html' import my_macro with context 
from flask import Flask, flash, redirect, render_template, \
     request, url_for

from ask1 import *
from review import *
from chat import *
from newpro import *
from place import *
from crawler import *
from crawlplace import *

app = Flask(__name__ )

	
@app.route('/')
def bh():
    return render_template('index.html')
	
@app.route('/backk', methods=['GET', 'POST'])
def backk():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('index.html')
	
@app.route('/bhakk' , methods=['GET', 'POST'])
def test():
    
    text=request.form.get('name')
    str1='hotels in '+text
    ct = ""
    req=crawler(str1)
    splt=text.split()
    size=len(splt)
    #sa = text[0]
    #sb = text[1:]
    #sa = sa.upper()
    #sb = sb.lower()
    #ct = sa+sb
    if size==1:
        sa = text[0]
        sb = text[1:]
        sa = sa.upper()
        sb = sb.lower()
        ct = sa+sb
    else:
        for i in splt:
            sa = i[0]
            sb = i[1:]
            sa = sa.upper()
            sb = sb.lower()
            ct += sa+sb
            ct += '_'
        ct = ct[:len(ct)-1]

    print "CTCTCTCTTCTCTCTTCCTTCTCTTCCTTCTCTTCTCTCTCTCTTCTTCTCTCCTTCTCTCTCTTCTCTCTCTTCT"
    print ct
    wiki="http://wikitravel.org/en/"+ct 
    f = 1
    todo = list()  

    response = requests.get(wiki)
    paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
    for para in paragraphs:
        st=para.text
        hi="[edit][add listing]"
                    #print st
					
        if st.find("Learn[edit]")!=-1:
			break
		
        if f==1 and st.find("Do[edit]")!=-1:
            f=2
            print "mil gaya"
        elif f==2:
            #print "sahi"
            #print "statement8*************************************************************************:"
            #print st
            #print hi
            if st.find(hi)==-1:
                #print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                sst = st.find("edit")
                #print sst
                if sst!=-1:
                    st = st[:sst]
                #print st
				
                if st.find("[")!=-1:
					print 'bb ki vines'
					print st
					continue
                todo.append(st)
                #print "sssfsfsg"
                #print st
                #print f
            else:
                #print "--------====================================================================="
                #print hi
                #print st
                print "matched"
                f=1

    karishmadict=req.garda()
    keys=karishmadict.keys()
    addr1=list()
    revw1=list()
    rate1=list()
    key1=list()
    addr2=list()
    revw2=list()
    rate2=list()
    key2=list()
    addr3=list()
    revw3=list()
    rate3=list()
    key3=list()
    addr4=list()
    revw4=list()
    rate4=list()
    key4=list()
    addr5=list()
    revw5=list()
    rate5=list()
    rofl=list()
    '''for i in keys:
        addr1.append(karishmadict[i][0])
        revw1.append(karishmadict[i][1])
        rate1.append(karishmadict[i][2])
        rofl.append(karishmadict[i][3])'''

    for i in keys:
    	cntt=0
    	if karishmadict[i][0]!= "No address found":
    		cntt+=1
    	if karishmadict[i][1]!= "NO Review":
    		cntt+=1
    	if karishmadict[i][2]!= "No rating":
    		cntt+=1
    	if cntt==3:
    		key1.append(i)
    		addr2.append(karishmadict[i][0])
        	revw2.append(karishmadict[i][1])
        	rate2.append(karishmadict[i][2])
        	
        if cntt==2:
        	key2.append(i)
    		addr3.append(karishmadict[i][0])
        	revw3.append(karishmadict[i][1])
        	rate3.append(karishmadict[i][2])
        	
        if cntt==1:
        	key3.append(i)
    		addr4.append(karishmadict[i][0])
        	revw4.append(karishmadict[i][1])
        	rate4.append(karishmadict[i][2])

        if cntt==0:
        	key4.append(i)
    		addr5.append(karishmadict[i][0])
        	revw5.append(karishmadict[i][1])
        	rate5.append(karishmadict[i][2])
        	
        rofl.append(karishmadict[i][3])

    addr1 = addr2+addr3+addr4+addr5
    revw1 = revw2+revw3+revw4+revw5
    rate1 = rate2+rate3+rate4+rate5
    keys=key1+key2+key3+key4

    print "length"
    print len(keys)
    print len(addr1)
    print len(revw1)
    print len(rate1)
    
    #print addr1
    #print revw1
    #print rate1
	
    str2='places to visit in '+text
    req1=crawlplace(str2,text)
    kareenadict=req1.garda()
    name=kareenadict.keys()
    ades=list()
    aplc=list()
    bplc=list()
    bdes=list()
    plc=list()
    desc=list()
    for item in name:
        if kareenadict[item] == "No desc":
            bplc.append(item)
            bdes.append(kareenadict[item])
        else:
            aplc.append(item)
            ades.append(kareenadict[item])
    plc=aplc+bplc
    desc=ades+bdes
    print len(plc)
    #print bplc
    print len(desc)
    print "0)0))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))"
    for i in todo:
        print i

    return render_template('bhakk.html',data= zip(keys,addr1,revw1,rate1,rofl),data1=zip(plc,desc),data2=todo,j=text.upper())
    #output = "<html><body>" + "<h1><p>%s</p></h1>" % (text1) + "</body></html>"    
    #return output


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=1112)