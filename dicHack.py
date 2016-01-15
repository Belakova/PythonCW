# Script: dicHack.py
#Author : Belakova
#Script : dicHack.py

import sys, hashlib, re
#working
def dict_attack(passwd_hash):
     
    
    #check if the file of passwords is correct
    #dic = open('dict.txt','r')
     
    dic = ['123','1234','12345','123456','1234567','joshua','12345678','password', 'qwerty','abc','abcd','abc123','111111','monkey','arsenal','letmein','trustno1','dragon','baseball','superman','iloveyou','starwars','montypython','cheese','123123','football','password','batman'] 
    #compare the hash of a pass in the dictionary
    print 'Cracking. . .  '
    for i in dic:
         
            md5hashObject = hashlib.md5(i)
            dictCompare = md5hashObject.hexdigest()
         
            match = re.search(dictCompare,passwd_hash)
            if match: 
                print 'Encryption:', i
       
              
