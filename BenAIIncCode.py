#importing modules
import time
import datetime
import random

#opening files and setting parameters
#info file
userinfo=open('c:/users/admin/desktop/abc.txt', 'r')
userlist=userinfo.readlines()
userinfo.close()
#joke file
jokefile=open('c:/users/admin/desktop/jokeben.txt', 'r')
jokelist=jokefile.readlines()
jokefile.close()

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

#startup code
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
      if order=="/bye/":
         break
      elif "joke" in order:
         while 1:
            jokenumber=int(random.randint(1, 206))
            if jokenumber % 2==0:
               pass
            else:
               print("\n"+jokelist[jokenumber][:-1]+"\n")
               break
