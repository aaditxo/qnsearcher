#!/usr/bin/python

import os
supportedlst=["Windows","Mac","Linux"]
print("Please select your operating system. Supported OSs are: ")
c=0
for i in supportedlst:
        c+=1
        print(c,"-",i)
osno=int(input("Your Choice: "))
osname=supportedlst[osno-1]
if osname=="Windows":
        browname=(input('''Enter the name of your browser: ''')).lower()

try:
        defile=open('defaults.stg','x')
        defile.close()
        defile=open('defaults.stg','w')
except:
        os.remove('defaults.stg')
        defile=open('defaults.stg','x')
        defile.close()
        defile=open('defaults.stg','w')
defaults=[]
if osname=="Windows":
        browmane="Browser :"+browname+'\n'
        defaults.append(browmane)
osmane="OS :"+osname
defaults.append(osmane)
defile.writelines(defaults)
defile.close()
defile=open('defaults.stg')
print('Your defaults have been set to\n',defile.read())
defile.close()
try:
        defile=open('defaults.stg','x')
        defile.close()
        defile=open('defaults.stg','w')
except:
        os.remove('defaults.stg')
        defile=open('defaults.stg','x')
        defile.close()
        defile=open('defaults.stg','w')
defaults=[]
osname=osname
if osname=="Windows":
        browname=browname+'\n'
        defaults.append(browname)
defaults.append(osname)
defile.writelines(defaults)
defile.close()
