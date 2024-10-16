import datetime

alarmhour = int(input("Enter Hour: ")) 
alarmMin = int(input("Enter Minutes: "))
alarmAm = str(input("am/pm: "))

if(alarmAM =="pm"):
    alarmhour = alarmhour + 12

while (1==1):
    if(alarmhour == datetime.datetime.now().hour and alarmMin== datetime.datetime.now().minute ):
        print("wake up now")
        break

print("exited")

