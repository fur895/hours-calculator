import csv
import time
import math

tempdata = []

with open('V5.csv', mode ='r')as file:
  csvfile = csv.reader(file)
  for row in csvfile:
        tempdata.append(row)
        
header = tempdata[0]
data = tempdata[1:]
##########################################
now = time.localtime()
datetime_format = "%a, %b %d %Y %H:%M:%S"
date_format = "%b %d %y"
time_format = "%H:%M:%S"
today = time.strftime(date_format,now)
current_time = time.strftime(time_format,now)
hours = [x for x in range(24)]
minutes = [x for x in range(60)]
##########################################
def hour_calc(h1,h2,calculation):
    days = 0
    if h1 > 23 or h2 > 23:
        print ("Hours out of range")
    if calculation == "-":
        ans = h1 - h2
        if ans > 23:
            days += ans//24
            ans = round((ans/24-days)*24)
        return hours[ans]
    elif calculation == "+":
        ans = h1 + h2
        if ans > 23:
            days += ans//24
            ans = round((ans/24-days)*24)
        return hours[ans]
    elif calculation == "*":
        ans = h1 * h2
        if ans > 23:
            days += ans//24
            ans = round((ans/24-days)*24)
        return hours[ans]
    elif calculation == "/":
        ans = h1 / h2
        if ans > 23:
            days += ans//24
            ans = round((ans/24-days)*24)
        return hours[ans]
    else:
        print ("Hour calculation Error")

print (hour_calc(7,122,"-"))

#def time_dif(start_time,end_time):
#    if isinstance(start_time,str) == True:
#        start_time = start_time.split(":")
#        for ind, ea in enumerate(start_time):
#            start_time[ind] = int(ea)
#    if isinstance(end_time,str) == True:
#        end_time = end_time.split(":")
#        for ind, ea in enumerate(end_time):
#            end_time[ind] = int(ea)