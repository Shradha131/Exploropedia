'''from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)
'''
#from 'bhakk.html' import my_macro with context 
from flask import Flask, flash, redirect, render_template, \
     request, url_for
#from search1 import *
from ask1 import *
from review import *
#api_key='AIzaSyCIkKdD7oKsN4voYBkUKNxBcnqYV6jwGLI'#jst abhi3
#api_key='AIzaSyC-9CByt2_vUGLWg1U2LXO_3oHad_wcJGY'#new1
#api_key= 'AIzaSyA3rkNptOlfjIt_tMW8Vo6AvjsjMdIMkC8' #neha
#api_key= 'AIzaSyCWstexStQ9VMx96OO4YIEJZnNGbh0EPTM' #satya
#api_key='AIzaSyBSQyHkX7_85R5f0w28RblQPbFX9CzwOdg'#b2
api_key='AIzaSyA8lAxzn2LuLxT6sOLPO1lwENeOmEyYn6Q'#nanu
#api_key='AIzaSyD-7z0_PVPNmbV0QMUeAFHO5juBDVMSsMU'#nya2
# Shradha
app = Flask(__name__ )
#gg='https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference='+img+'&key='+api_key
@app.route('/')
def bh():
    return render_template('index.html')

@app.route('/bhakk' , methods=['GET', 'POST'])
def test():
    text=request.form.get('name')
    #return text
   # print 3
    #processed_text = text
    #return text
    tex1='hotels in '+text
    print "heyaaaaaa"
    request1 = Ask1(tex1.lower())
    text1=''
    if text1 == '' and api_key != '':
        text1 = request1.google_response(api_key)
    tex2='museum in '+text
    request2 = Ask1(tex2.lower())
    text2=''
    if text2 == '' and api_key != '':
        text2 = request2.google_response(api_key)
    tex3='religious places in '+text
    request3 = Ask1(tex3.lower())
    text3=''
    if text3 == '' and api_key != '':
        text3 = request3.google_response(api_key)
    tex4='shopping malls in '+text
    request4 = Ask1(tex4.lower())
    text4=''
    if text4 == '' and api_key != '':
        text4 = request4.google_response(api_key)
    tex5='pubs and bars in '+text
    request5 = Ask1(tex5.lower())
    text5=''
    if text5 == '' and api_key != '':
        text5 = request5.google_response(api_key)
    tex6='chemist in '+text
    request6 = Ask1(tex6.lower())
    text6=''
    if text6 == '' and api_key != '':
        text6 = request6.google_response(api_key)
    #cc='<br>'
    #text1.replace('\n',cc)
    #naam=text1.split('#')
    #print naam

    dd=text1[0].split('$')
    g = text1[1].split('#')
    foto1=text1[2].split('@')
    r1=text1[3].split('*')
    rvname = []
    rvtext = []
    rvsite = []
    rvmap = []
    rvfone = []
    rvvic = []
    #rvopn = []
    #print "kro"
    #print r1
    
    k=len(r1)
    k-=1
    print "Hotel Length : "
    print k
    l=7
    if k<7:
        l=k
    for var in r1[0:l]:
        #tex7 = var
    #    print var
        request7 = review(var)
        text7 = ''
        if text7 == '' and api_key != '':
            text7 = request7.google_response(api_key)
        rvsplit = text7[0].split('*')
        #rvname.append([])
        rvname.append(rvsplit)
        rvtextsplit = text7[1].split('*')
        #rvtext.append([])
        rvtext.append(rvtextsplit)
        rvmap.append(text7[3])
        rvsite.append(text7[2])
        rvfone.append(text7[4])
        rvvic.append(text7[5])
        #rvopn.append(text7[6])
    #print "map:"
    #print rvname
    c=[]
    for img in foto1:
        if(img=='yo'):
            c.append('http://www.hotel-r.net/im/hotel/asia/hk/hotel-icon-10.png')
            #c+= '@'
        else:
            c.append('https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + img + '&key=' + api_key)
            #c+= '@'
    #c=c.split('@')
    dd1=text2[0].split('$')
    g1 = text2[1].split('#')
    foto2 = text2[2].split('@')
    r2 = text2[3].split('*')
    rvname1 = []
    rvtext1 = []
    rvsite1 = []
    rvmap1 = []
    rvfone1 = []
    rvvic1 = []
    #rvopn1 = []
    #print "kro"
    #print r1
    
    k=len(r2)
    k-=1
    print "Museum Length : "
    print k
    l=7
    if k<7:
        l=k
    for var in r2[0:l]:
        #tex7 = var
     #   print var
        request8 = review(var)
        text8 = ''
        if text8 == '' and api_key != '':
            text8 = request8.google_response(api_key)
        rvsplit1 = text8[0].split('*')
        #rvname.append([])
        rvname1.append(rvsplit1)
        rvtextsplit1 = text8[1].split('*')
        #rvtext.append([])
        rvtext1.append(rvtextsplit1)
        rvmap1.append(text8[3])
        rvsite1.append(text8[2])
        rvfone1.append(text8[4])
        rvvic1.append(text8[5])
        #rvopn1.append(text8[6])
    #print "map:"
    #print rvname
    c1 = []
    for img in foto2:
        if (img == 'yo'):
            c1.append('https://thumb1.shutterstock.com/display_pic_with_logo/134038/433157668/stock-vector-museum-icon-isolated-on-white-background-museum-logo-vector-symbol-433157668.jpg')
            # c+= '@'
        else:
            c1.append(
                'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + img + '&key=' + api_key)
            # c+= '@'
    dd2=text3[0].split('$')
    g2 = text3[1].split('#')
    foto3 = text3[2].split('@')
    r3 = text3[3].split('*')
    rvname2 = []
    rvtext2 = []
    rvsite2 = []
    rvmap2 = []
    rvfone2 = []
    rvvic2 = []
    #rvopn2 = []
    #print "kro"
    #print r1
    
    k=len(r3)
    k-=1
    print "Holy Length : "
    print k
    l=7
    if k<7:
        l=k
    for var in r3[0:l]:
        #tex7 = var
      #  print var
        request8 = review(var)
        text8 = ''
        if text8 == '' and api_key != '':
            text8 = request8.google_response(api_key)
        rvsplit1 = text8[0].split('*')
        #rvname.append([])
        rvname2.append(rvsplit1)
        rvtextsplit1 = text8[1].split('*')
        #rvtext.append([])
        rvtext2.append(rvtextsplit1)
        rvmap2.append(text8[3])
        rvsite2.append(text8[2])
        rvfone2.append(text8[4])
        rvvic2.append(text8[5])
        #rvopn2.append(text8[6])
   # print "map:"
  #  print rvname
    
    c2 = []
    for img in foto3:
        if (img == 'yo'):
            c2.append('https://image.freepik.com/free-icon/church-black-silhouette-with-a-cross-on-top_318-50365.jpg')
            # c+= '@'
        else:
            c2.append(
                'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + img + '&key=' + api_key)
            # c+= '@'
    dd3=text4[0].split('$')
    g3 = text4[1].split('#')
    foto4 = text4[2].split('@')
    r4 = text4[3].split('*')
    rvname3 = []
    rvtext3 = []
    rvsite3 = []
    rvmap3 = []
    rvfone3 = []
    rvvic3 = []
    #rvopn3 = []
    #print "kro"
    #print r1
    
    k=len(r4)
    k-=1
    print "Mall Length : "
    print k
    l=7
    if k<7:
        l=k
    for var in r4[0:l]:
        #tex7 = var
    #    print var
        request8 = review(var)
        text8 = ''
        if text8 == '' and api_key != '':
            text8 = request8.google_response(api_key)
        rvsplit1 = text8[0].split('*')
        #rvname.append([])
        rvname3.append(rvsplit1)
        rvtextsplit1 = text8[1].split('*')
        #rvtext.append([])
        rvtext3.append(rvtextsplit1)
        rvmap3.append(text8[3])
        rvsite3.append(text8[2])
        rvfone3.append(text8[4])
        rvvic3.append(text8[5])
        #rvopn3.append(text8[6])
    #print "map:"
    #print rvname
    
    c3 = []
    for img in foto4:
        if (img == 'yo'):
            c3.append('https://cdn4.iconfinder.com/data/icons/building-1/512/build21-512.png')
            # c+= '@'
        else:
            c3.append(
                'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + img + '&key=' + api_key)
            # c+= '@'
    dd4=text5[0].split('$')
    g4 = text5[1].split('#')
    foto5 = text5[2].split('@')
    r5 = text5[3].split('*')
    rvname4 = []
    rvtext4 = []
    rvsite4 = []
    rvmap4 = []
    rvfone4 = []
    rvvic4 = []
    #rvopn4 = []
    #print "kro"
    #print r1
    
    k=len(r5)
    k-=1
    print "Pubs Length: "
    print k
    l=7
    if k<7:
        l=k
    for var in r5[0:l]:
        #tex7 = var
     #   print var
        request8 = review(var)
        text8 = ''
        if text8 == '' and api_key != '':
            text8 = request8.google_response(api_key)
        rvsplit1 = text8[0].split('*')
        #rvname.append([])
        rvname4.append(rvsplit1)
        rvtextsplit1 = text8[1].split('*')
        #rvtext.append([])
        rvtext4.append(rvtextsplit1)
        rvmap4.append(text8[3])
        rvsite4.append(text8[2])
        rvfone4.append(text8[4])
        rvvic4.append(text8[5])
        #rvopn4.append(text8[6])
    #print "map:"
    #print rvname
    
    c4 = []
    for img in foto5:
     #   print img
        if (img == 'yo'):
            c4.append('https://desertviewinn.com/wp-content/uploads/2013/04/pub_bar-09-512.png')
            # c+= '@'
        else:
            c4.append(
                'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + img + '&key=' + api_key)
            # c+= '@'
    dd5=text6[0].split('$')
    g5 = text6[1].split('#')
    foto6 = text6[2].split('@')
    r6 = text6[3].split('*')
    rvname5 = []
    rvtext5 = []
    rvsite5 = []
    rvmap5 = []
    rvfone5 = []
    rvvic5 = []
    #rvopn5 = []
    #print "kro"
    #print r1
    
    k=len(r6)
    k-=1
    print "mai itta hi bda  chemist: "
    print k
    l=7
    if k<7:
        l=k
    for var in r6[0:l]:
        #tex7 = var
      #  print var
        request8 = review(var)
        text8 = ''
        if text8 == '' and api_key != '':
            text8 = request8.google_response(api_key)
        rvsplit1 = text8[0].split('*')
        #rvname.append([])
        rvname5.append(rvsplit1)
        rvtextsplit1 = text8[1].split('*')
        #rvtext.append([])
        rvtext5.append(rvtextsplit1)
        rvmap5.append(text8[3])
        rvsite5.append(text8[2])
        rvfone5.append(text8[4])
        rvvic5.append(text8[5])
        #rvopn5.append(text8[6])
    #print "map:"
    #print rvname
    
    c5 = []
    for img in foto6:
        if (img == 'yo'):
            c5.append('http://www.hotel-r.net/im/hotel/asia/hk/hotel-icon-10.png')
            # c+= '@'
        else:
            c5.append(
                'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + img + '&key=' + api_key)
            # c+= '@'
    #print text1
   # print c[0]
    return render_template('bhakk.html',data= zip(dd,g,c,rvname,rvtext,rvsite,rvmap,rvfone,rvvic,dd1,g1,c1,rvname1,rvtext1,rvsite1,rvmap1,rvfone1,rvvic1,dd2,g2,c2,rvname2,rvtext2,rvsite2,rvmap2,rvfone2,rvvic2,dd3,g3,c3,rvname3,rvtext3,rvsite3,rvmap3,rvfone3,rvvic3,dd4,g4,c4,rvname4,rvtext4,rvsite4,rvmap4,rvfone4,rvvic4,dd5,g5,c5,rvname5,rvtext5,rvsite5,rvmap5,rvfone5,rvvic5),j=text.upper())
    #output = "<html><body>" + "<h1><p>%s</p></h1>" % (text1) + "</body></html>"    
    #return output


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=1112)