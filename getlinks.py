#Coursework2 Application Development
#Author: Belakova
#Script: getlinks.py
#URL Analysis: http://www.soc.napier.ac.uk/~cs342/CSN08115/cw_webpage/index.html

import urllib, sys, re, hashlib
import getweb
 

#Get http and https
#working
def print_links(page):
          # regex to match on hyperlinks, returning 3 grps, links[1]          
          links = n = re.findall(r'\https?://[/?\daA-zZ\.-]+',page)
          # sort and print the links
          links.sort()
          print  str(len(links)), 'HyperLinks Found:'
          for link in links:
              print link

             
#Email addresses
#working              
def getmails(page):  
     emails = re.findall(r'[\w+\d+._+-]+@[\w+\d+._+-]+\.[a-z]{2,}',page) 
     for email in emails:
          print email
        
#Get list of password hashes
#working    
def getpasswords(page):
     psws = re.findall(r'([a-fA-F\d]{32})', page)      
     for line in psws:
            print line
     return psws        #returns the list of found hashes for the following analysis
           
  
             
     
            

#Phone numbers
#working
def getnumbers(page): 
    numbers = re.findall(r'(\+\d{2}\(\d\)??\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4})',page)
    for number in numbers:
        print 'Found: ' + number
   


 



