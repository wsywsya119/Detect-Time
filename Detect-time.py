# -*- coding: utf-8 -*-

import re
import time
import datetime


def detectDate(data):

    numWord = "0-9,一二三四五六七八九十兩"
    dayWord = "明前後隔天日號"
    pamWord = "上午中午下午晚上"

    timePat = "["+numWord+"]*[年/]*["+numWord+"]*[月/]*["+numWord+"]*["+dayWord+"]*["+pamWord+"]*["+numWord+"]*[點時:]*["+numWord+"]*分?"

    time = re.findall(timePat,data)
    print(time)
    #print(time.strptime(data, "%H:%M:%S"))
    


def main():
    detectDate("我七月三十去打球明天下午2:13去游泳")

if __name__ == "__main__":
    main()
