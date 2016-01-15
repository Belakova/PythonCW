#Coursework2 Application Development
#Author : Belakova
#Script:  getweb.py
#URL Analysis: http://www.soc.napier.ac.uk/~cs342/CSN08115/cw_webpage/index.html

 
import urllib, sys, re, urllib2, os

#Script is calling following Scripts
import getlinks     #regex for emails,numbers,paswords
import dicHack      #cracking found hashed passwords in the URL 
import getDocs      #regex for the files to be downloaded (links,images,docs)
import directories  #file downloading, creating and listing the directories,  Forensic Analysis
 

def getweb(url):
     try:
          webpage = urllib.urlopen(url) 
          content = webpage.read()
          return content
     except:
          print 'Exception: Cannot access URL address'
 
def main():
     # temp testing url argument
     sys.argv.append('http://www.soc.napier.ac.uk/~cs342/CSN08115/cw_webpage/index.html')

     # Check args
     if len(sys.argv) != 2:
          print '[-] Usage: cw(1) URL'
          return
  
       
      #Get the web page and check if the calling script exists
     try: 
          page = getweb(sys.argv[1])
          
     except:
          print 'Error with openning the Script getlinks.py'


     
      
     #REGEX for emails, links, mobiles phones, hash paswords and password cracking
    
     try:
          links = getlinks.print_links(page)
          emails = getlinks.getmails(page)
          passwords = getlinks.getpasswords(page)
          
          for y in passwords:                
               passwordEncryption = dicHack.dict_attack(y)
          
                
     except:
          print 'error with openning getlinks Script'
     '''''' 
     
     ####### UNCOMMENT for the following analysis
     #REGEX for files, make directory, download files, check them 
     ''' 
      
     try:
          pics = getDocs.getpics(page)                      #regex for files jpg,gif,bmp,docx
          try:
               courseworkDir = directories.createDir()  #Check if c:temp//coursework directory exists
               for i in pics:     
                    Filename = directories.downloadFiles(i) #Downloading all links            
               CheckFolder =  directories.checkFileinDir() #to list the content of a directory 
               directories.ForensicAnalysis()              #bad hashes  analysis

          except:
               print 'error with openning Script directories.py'
     except:
          print 'error with openning Script getDocs.py'
     '''    
     
if __name__ == '__main__':
         main()
