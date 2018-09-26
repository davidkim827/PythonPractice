#!/usr/bin/env python3

import json, os, calendar
from collections import Counter

realPath = os.path.realpath("famousPeopleBirthday.json")
with open(realPath, 'r') as f:
    info = json.load(f)
monthCountDict = {}

def monthCounter():
    for month in monthCountDict.keys():
        if monthCountDict[month] > 0:
            print("\"{:>3}\" : {},".format(month, monthCountDict[month]))
    
def createMonthCountDict():
    monthArray = calendar.month_abbr
    
    for eachMonth in range(1,13):
        monthCountDict[monthArray[eachMonth]] = 0
        
    for eachPerson in info:
        dates = info[eachPerson]
        separateDate = dates.split('/')
        birthMonth = int(separateDate[0])
        
        for month in monthCountDict.keys():
            if month == monthArray[birthMonth]:
                monthCountDict[month]+=1

createMonthCountDict()
monthCounter()