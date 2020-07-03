#!/usr/bin/python

import os
noofqns=0
print("Hello, you are using qnsearcher version 1.0.5. To change your defaults, run setup.py again. \n")
qns=input("Enter the TXT file containing the questions :")
qnos=int(input("Enter an approximate number of questions in an integer form: "))
pref=''
pref=input("Enter any extra keyterm to search with every question (If none, hit enter):")
defile=open('defaults.stg')
deflie=defile.read()
defaults=deflie.split('\n')
try:
        osname=defaults[1]
except:
        osname=defaults[0]
if osname=="Windows":
        browname="start "+defaults[0]
elif osname=="Linux" or osname=="Mac":
        browname='xdg-open'
defile.close()
file=open(qns)
qbank=file.read()
qlst=qbank.split('\n')
nulist=[]
for i in range(1,qnos+5):
        nulist.append(i)
for qn in qlst:
        qorno=False
        for j in nulist:
                if qorno==False:
                        if str(j) in qn:
                                qorno=True
                        
        if qorno==True:
                noofqns+=1
                finalq=''
                for j in qn:
                        if j==' ':
                                ch='%20'
                        else:
                                ch=j
                        finalq+=ch
                finalq+=pref
                searchformat=browname+" https://www.google.com/search?q="+finalq
                os.system(searchformat)
print("Searched",noofqns,"questions.")
input()