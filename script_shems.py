# -*- coding: iso-8859-1 -*-
from boilerpipe.extract import Extractor
from bs4 import BeautifulSoup
import codecs
from json import dumps
import urllib2
import sys
#from urllib import request as R
page = urllib2.urlopen(str(sys.argv[1])).read()
#f = open('workfile.json', 'a')
#print 'Argument List:', str(sys.argv[1])
listArticle=[]
def praseOne(element):
	d=dict()
	linkA="http://www.mosaiquefm.net"+element.a["href"]
	#print type(linkA)
	utf8string = linkA.encode("utf-8")
	#print "***************************"
	#print utf8string
	#print "***************************"
	extractor = Extractor(extractor='ArticleExtractor', url=utf8string)
	text=extractor.getText()
	print "text" + text.encode("utf-8")
	d["Article"]=text.encode("utf-8")
	d["titleArticle"]= element.a["title"]
	print "title" + element.a["title"]
	d["linkImg"]=element.img["src"]
	print "image" + element.img["src"]
	listArticle.append(d)


soup = BeautifulSoup(page,'html.parser')

for i in soup.findAll('div',{'class':'thumb'}):
    praseOne(i)

""" f=codecs.open("/var/www/news/"+str(sys.argv[2])+".json",'w',"utf-8")
f.write('{ "Articles": [')
c=0
for i in soup.findAll('div',{'class':'intro'}):
    listArticle[c]["Description"]=i.contents[0]
    #print(dumps(listArticle[c]))
    f.write(dumps(listArticle[c]))
    if c < len(listArticle) - 1 :
        f.write(",\n")
    c+=1

f.write("] \n }")
f.close()

#hi people
"""
