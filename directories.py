#Coursework2 Application Development
#Author : Belakova
#Script:  directories.py
#URL Analysis: http://www.soc.napier.ac.uk/~cs342/CSN08115/cw_webpage/index.html

import urllib, sys, re, os, hashlib
   
def checkFileinDir():
    dirname = 'c:\\temp\\coursework'
    files = os.listdir(dirname)
    for fname in files:
        path = os.path.join(dirname, fname)
        print os.path.abspath(path)
 
     
def createDir():
    dirname = 'c:\\temp\\coursework'
    try:
        os.makedirs(dirname)
        print 'Directory has been created'
    except OSError:
        if os.path.exists(dirname):
            print 'c:temp//coursework already exists'
            # We are nearly safe
            pass
        else:
            print 'c:temp//coursework did not exist'
            # There was an error on creation, so the error appears
            raise

def downloadFiles(Filename):
    try:
         dirname = 'c:\\temp\\coursework'
         name = os.path.join(dirname,Filename)
         if os.path.exists(name):
            
             
             try:
                 readFile = open(name,'r')
                 readFile.read()
                 readFile.close() 
                 print 'File already exists', Filename 

             except:
                 print 'not readable file'
                 
               
             
         else:
             f = open(name,'wb')
             f.write(urllib.urlopen('http://www.soc.napier.ac.uk/~cs342/CSN08115/cw_webpage/'+Filename).read())
             f.close()     
             print 'File Downloaded' , Filename
             return Filename
    except:
         print 'Error with downloading a file ' , Filename

 
def ForensicAnalysis():
    try:
         base_path = 'c:\\temp\\coursework'
         #create a dictionary of the bad hashes to compare with
         badHash = {'9d377b10ce778c4938b3c7e2c63a229a':'contraband_file1.jpg','6bbaa34b19edd6c6fa06cccf29b33125':'contraband_file2.jpg','e4e7c3451a35944ca8697f9f2ac037f1':'contraband_file3.jpg','1d6d9c72e3476d336e657b50a77aee05':'contraband_file4.gif'}

         for root, dirs, files in os.walk(base_path):
                for file_str in files:
                   file_obj = file(os.path.join(root, file_str))
                   file_md5 = hashlib.md5(file_obj.read()).hexdigest()      #hash of the content of a file
                   hashName = hashlib.md5(file_str)                         #md5 object
                   nameH = hashName.hexdigest()                             #hash of the name of a file
                    

                   if file_md5 and hashName in badHash:
                       print 'bad'
                   else:
                       print 'the file %s is safe' %file_str
 
    except IOError:
         print 'Error openning'
    
