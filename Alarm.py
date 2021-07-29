from datetime import datetime

from django.core.serializers import python
from playsound import playsound

alarmtime = input("Enter the time of Alarm: HH:MM:SS AM/PM \n")

alarmhour = alarmtime[0:2]

alarmminute = alarmtime[3:5]

alarmsecond = alarmtime[6:8]

alarmperiod = alarmtime[9:].upper()

while True:
    def validate(alarmtime):
        if len(alarmtime) != 11:
            return "Invalid time format"

        else:
            if int(alarmsecond) > 59:
                return "invalid second format"
            elif int(alarmhour) > 12 :
                return "invalid Hour format"
            elif int(alarmminute) > 59 :
                return "invalid Minute format"
            else:
                return "Perfectly Fine"
    
while True:
    alarmtime = input("Enter the time of Alarm: HH:MM:SS AM/PM \n")

    validate_check = validate(alarmtime.lower())
   
    if validate_check != "Perfectly Fine":
        print(validate_check)
    else:
        print(F"Setting the alarm for"+ alarmtime)
        break

    now = datetime.now()
    currenthour = now.strftime("%I")
    currentmin = now.strftime("%M")
    currentsecond = now.strftime("%S")
    currentperiod = now.strftime("%p")

    if alarmperiod == currentperiod:
        if alarmhour == currenthour:
            if alarmminute == currentmin:
                if alarmsecond == currentsecond:
                    print("WAKE UP")
                    playsound('C:\Users\hp\Desktop\Python projects 1\python alarm sound.wav')
                    break
                



