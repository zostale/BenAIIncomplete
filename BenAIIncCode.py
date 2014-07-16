#This is my canvas, this is my art.

"""
Name:                         Benedict&Pack
Version:                      1.0
Author:                       Nirman Dave
Description:                  An artificial intelligence system that conducts basic functions.
                              The package allows anyone to replicate this system, using few
                              lines of code and embed into apps.
Publisher:                    SourceNet
Publisher's website:          www.sourcenet.in

Copyright notice, terms & conditions:
(c) Copyrights 2014 by Nirman Dave. All rights reserved.
This work may be modified, reproduced, distributed, performed, and displayed for any purpose
but must acknowledge "Nirman Dave", "SourceNet" and "Benedict&Pack". Copyright is retained
and must be preserved. The work is provided as is; no warranty is provided, and users accept all
the liability.
"""

#importing modules
import time
import datetime
import random
import pywapi
import string

#opening files and setting parameters
#info file
userinfo=open('d:/Softwares/Nirman\'s Python/Benedict/Benedict/FILES/maininfo.txt', 'r')
userlist=userinfo.readlines()
userinfo.close()
#joke file
jokefile=open('d:/Softwares/Nirman\'s Python/Benedict/Benedict/FILES/jokeben.txt', 'r')
jokelist=jokefile.readlines()
jokefile.close()
#dislike words file
dislikefile=open('d:/Softwares/Nirman\'s Python/Benedict/Benedict/FILES/dislikewords.txt', 'r')
dislikelist=dislikefile.readlines()
dislikefile.close()

#defining variables
datefix=str(datetime.datetime.now().strftime("%d-%m"))
uname=userlist[0][:-1]
usurname=userlist[1][:-1]
udate=userlist[2][:-1]
umonth=userlist[3][:-1]
uyear=userlist[4][:-1]
ugender=userlist[5][:-1]
umail=userlist[6][:-1]
upassword=userlist[7][:-1]
me='benedict'
mes='ben'

#startup code & greetings
dislikelist2=[]
for item in dislikelist:
    dislikelist2.append(item[:-1])
if uname=='First name' or uname=='' or usurname=='Last name' or udate=='DD' or upassword=='Password' or upassword=='':
   raw_input("Before you start using Benedict, please update your personal information using the 'Benedict AI - Settings' dialog. Press enter to exit.")
   toggle="1"
elif str(udate+"-"+umonth)==datefix:
    print("Hello "+str(uname)+", HAPPY BIRTHDAY! I am Benedict, how should I help you?")
    toggle="0"
else:
    print("Hello "+str(uname)+"! I am Benedict, how should I help you?\n")
    toggle="0"

#main command line
while 1:
   if toggle=="1":
      break
   else:
      order1=raw_input(">>>| ")
      order=str(order1.lower())

#Ending Code
      if order=="/bye/":
         break

#Joke Code
      elif "joke" in order:
         if any(item in order for item in dislikelist2):
            print "\nWhy not?\n"
         else:
            while 1:
               jokenumber=int(random.randint(1, 206))
               if jokenumber % 2==0:
                  pass
               else:
                  print ("\n"+jokelist[jokenumber][:-1]+"\n")
                  break
                
#Weather code
      elif "weather in" in order:
          weatherstring=order.index('n')
          weatherlocation=order[(int(weatherstring)+2):]
          lookup = pywapi.get_location_ids(weatherlocation)
          for i in lookup:
              location_id = i
          weather_com_result = pywapi.get_weather_from_weather_com(location_id)
          print "\nIt is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "*C now in " + weatherlocation + "\n"
      elif "weather of" in order:
          weatherstring=order.index('f')
          weatherlocation=order[(int(weatherstring)+2):]
          lookup = pywapi.get_location_ids(weatherlocation)
          for i in lookup:
              location_id = i
          weather_com_result = pywapi.get_weather_from_weather_com(location_id)
          print "\nIt is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "*C now in " + weatherlocation + "\n"
          
#Math functions code all
    #math

#Math pattern indentifier
    #pattern

#Reminder code
    #reminders

#Colloquial 
    #colloquial response (time consuming)

#Search code
    #search things in computer and open if defined

#Web and surf code
    #codes to surf the web, search images, videos this and that!
