import re


def detectPeriod(data):
    
    numWord = "[0-9,一二三四五六七八九十兩半]"
    hourWord = "小時鐘頭"
    minWord = "分鐘"
    secWord = "秒鐘"


    timePat = "["+numWord+"]+點?\.?["+numWord+"]*個?半?["+hourWord+"]*半?又?["+numWord+"]*["+minWord+"]*又?["+numWord+"]*["+secWord+"]*"




def main():
    detectPeriod("我要去游泳一個小時")

if __name__ == "__main__":
    main()
