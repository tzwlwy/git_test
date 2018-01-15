
from selenium import webdriver
import time
import os
import sys
dr = webdriver.Chrome("chromedriver.exe")
dr.get('https://www.baidu.com/')
time.sleep(1)
dr.close()
a=os.getcwd()
with open(r'D:\PHOTO\曾松点开看看123.txt', 'wt') as fout:
   fout.write(a)

