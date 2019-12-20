# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:00:01 2019

@author: Rishabh Sood
"""
import hashlib
print("Do you wish to: \n1. Hash Crack \n2. Hash Encrypt  ?\n")
ch = input("\nEnter choice: ")

def hashcrypt():
    print("What kind of hashing?:\n") 
    print("1. md5\n2. sha1\n3. sha224\n4. sha256\n5. sha384\n6. sha512")
    x = input("\nEnter your choice: ")
    
    def hmd5(str):
        result = hashlib.md5(str.encode())
        print(str + " = " + result.hexdigest())
    def hsha1(str):
        result = hashlib.sha1(str.encode())
        print(str + " = " + result.hexdigest())
    def hsha224(str):
        result = hashlib.sha224(str.encode())
        print(str + " = " + result.hexdigest())
    def hsha256(str):
        result = hashlib.sha256(str.encode())
        print(str + " = " + result.hexdigest())
    def hsha384(str):
        result = hashlib.sha384(str.encode())
        print(str + " = " + result.hexdigest())
    def hsha512(str):
        result = hashlib.sha512(str.encode())
        print(str + " = " + result.hexdigest())
        
    hash_dict = {
            "1": hmd5,
            "2": hsha1,
            "3": hsha224,
            "4": hsha256,
            "5": hsha384,
            "6": hsha512
            }
    
    vict = input("\nEnter the string to be Hashed: ")
    hash_dict[x](vict)
    
def hashcrack():
    load_wordlist = open(r"mywordlist.txt", "r")
    guess = load_wordlist.readline()
    inpt = input("Enter hash: ")
    k = 0
    
    while guess:
        clr = guess.strip()
        attempt = hashlib.md5(clr.encode())
        mystr = attempt.hexdigest()
        if(mystr == inpt):
          print(guess)
          k = 1
          break
        attempt = hashlib.sha1(clr.encode())
        mystr = attempt.hexdigest()
        if(mystr == inpt):
          print(guess)
          k = 1
          break
        attempt = hashlib.sha224(clr.encode())
        mystr = attempt.hexdigest()
        if(mystr == inpt):
          print(guess)
          k = 1
          break
        attempt = hashlib.sha256(clr.encode())
        mystr = attempt.hexdigest()
        if(mystr == inpt):
          print(guess)
          k = 1
          break
        attempt = hashlib.sha384(clr.encode())
        mystr = attempt.hexdigest()
        if(mystr == inpt):
          print(guess)
          k = 1
          break
        attempt = hashlib.sha512(clr.encode())
        mystr = attempt.hexdigest()
        if(mystr == inpt):
          print(guess)
          k = 1
          break
        guess = load_wordlist.readline()
        
    if k == 0:
        print("attempt failure!")
        
main_dict = {
        "1": hashcrack, 
        "2": hashcrypt
        }

main_dict[ch]()
1