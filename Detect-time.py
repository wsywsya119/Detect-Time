# -*- coding: utf-8 -*-

import re
import time
import datetime


def detectDate(data):

    numWord = "0-9,一二三四五六七八九十兩"
    dayWord = "明前後隔天日號"
    pamWord = "上午中午下午晚上"

    timePat = "["+numWord+"]*[年/-]?["+numWord+"]*[月/-]?["+numWord+"]*["+dayWord+"]*["+pamWord+"]*["+numWord+"]*[點時:]?["+numWord+"]*分?"     

    datePat = "["+numWord+"]*[/-]{1}["+numWord+"]*[/-]?["+numWord+"]*"

    yearPat = "["+numWord+"]+(?=年)"
    monPat = "["+numWord+"]+(?=月)"
    dayPat = "["+numWord+"]+(?=日|號)"

    #time = re.findall(timePat,data)
    #print(time)

    dateTime = re.findall(datePat,data)
    print(dateTime)

    for i in dateTime:
        print(i.find("-"))
        #print(time.strptime(i, "%m-%d"))
    


def main():
    detectDate("2012-12-21去打球明天下午2:13去游泳")

if __name__ == "__main__":
    main()
