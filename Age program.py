# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:04:58 2022

@author: hamada compoo
"""

import datetime


print(datetime.datetime.now().date())

print("Hello")
name = input("Enter Your Name : ")
print ("welcome " + name +" !")
dayofbirth = int (input("Enter Your Day of Birth : "))
monthofbirth = int (input("Enter Your Month of Birth : "))
yearofbirth = int (input("Enter Your Year of Birth : "))

age = int (input("Enter Your age now is : "))
            # datetime= (dayofbirth,monthofbirth,yearofbirth)


            # dateNow=datetime.datetime().now()       
            # mybirthday=int(input("Enter Your Birthday : "))
            # mybirthday= datetime.datetime()
            # print(dateNow - mybirthday)


#determine age 
monthes = age * 12
weeks = monthes * 4
days = age *365
hours = days * 24
minutes = hours * 60
seconds= minutes * 60
if (age<=15) :
    print ("welcome son !") 
elif (age>=16) and (age<=25) :
    print("welcome my friend !")
else :
    print("welcome dear!") 
print( name + f" Your age =  {age} Years " )
print( name + f" Your age = {monthes} Monthes " )
print( name +  f" Your age = {weeks} Weeks " )
print( name + f" Your age = {days} Days ")
print( name +  f" Your age = {hours} Hours ")
print( name + f" Your age = {minutes} Minutes ")
print( name +  f" Your age = {seconds} Seconds ")
       
