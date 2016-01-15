#Coursework2 Application Development
#Script:    getDocs.py
#URL Analysis: http://www.soc.napier.ac.uk/~cs342/CSN08115/cw_webpage/index.html
import getweb
import urllib, sys, re

#working regex
def getpics(page):  
     docs = re.findall(r'[\daA-zZ-]+\.(?:jpg|gif|bmp|docx)',page) 
     #for name in docs:
          #print  
          #print name  ##for Demo uncomment
     return docs
 
     
