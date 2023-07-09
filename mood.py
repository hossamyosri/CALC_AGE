# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 17:01:49 2022

@author: hamada compoo
"""
name = input("Enter Your Name : ")
print ("welcome " + name +" !")
age = int (input("Enter Your age : "))
if (age<=15) :
    print ("welcome son !") 
elif (age>=16) and (age<=25) :
    print("welcome my friend !")
else :
    print("welcome dear!")
    print ("How are you " +name )
mood = input()
mood1 =  "good" , "fine" , "nice"  , " كويس",  " تمام " , " تمم "
if mood in mood1:
    print ("good news , enjoy " + name)
else :
    print (" Don't worry , every thing will be ok " + name )
    