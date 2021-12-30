
#constant assignment
def add_time(start, duration,day="none"):
    startTime = start.split(":")
    starthHour = int(startTime[0])
    startMinute = int(startTime[1][0:2])
    startPeriod = startTime[1][-2:].lower()
    day = day.lower()
    daysPassed = 0
    dayNum = 0
    if startPeriod == "am":
        nextPeriod = "pm"
    else:
        nextPeriod="am"
        daysPassed =0.5
    
    print(daysPassed)

    if day == "monday":
        dayNum = 1
    elif day == "tuesday":
        dayNum = 2
    elif day == "wednesday":
        dayNum = 3
    elif day == "thursday":
        dayNum = 4
    elif day == "friday":
        dayNum = 5
    elif day == "saturday":
        dayNum = 6
    elif day == "sunday":
        dayNum = 7


    durationTime = duration.split(":")
    durationHour = int(durationTime[0])
    durationMinute = int(durationTime[1][0:2])

    finalHour = 0
    finalMinute = 0
    bool = True



    #calculation

    finalMinute = startMinute + durationMinute
    finalHour = durationHour + starthHour
    if finalMinute >= 60:
        finalMinute -= 60
        finalHour += 1

    while finalHour >= 12:
        if finalHour > 12 :
            finalHour -= 12 
            bool = not bool
            daysPassed += 0.5
        if finalHour == 12:
            bool = not bool
            daysPassed += 0.5
            break

    dayNum += round(daysPassed)
    while dayNum > 7:
        dayNum -= 7

    finalPeriod = startPeriod if bool else nextPeriod
    if day != "none":
        if dayNum == 7:
            day = "Sunday"
        elif dayNum == 6:
            day = "Saturday"
        elif dayNum == 5:
            day = "Friday"
        elif dayNum == 4:
            day = "Thursday"
        elif dayNum == 3:
            day = "Wednesday"
        elif dayNum == 2:
            day = "Tuesday"
        elif dayNum == 1:
            day = "Monday"
    finalDayStatement = ""

    if round(daysPassed) == 0:
        finalDayStatement = ""
    elif round(daysPassed) == 1:
        finalDayStatement = " (next day)"
    else:
        finalDayStatement = f' ({round(daysPassed)} days later)'
    




        



    if len(str(finalMinute)) < 2:
      strMinute = "0" + str(finalMinute)
    else: 
      strMinute = str(finalMinute)

    if day == "none":
      finale = str(finalHour)+":"+strMinute+" "+finalPeriod.upper()+finalDayStatement
    else:
      finale = str(finalHour)+":"+strMinute+" "+finalPeriod.upper()+","+" "+day+finalDayStatement
  

    return(finale)


print(add_time("3:30 PM", "2:12", "Monday"))