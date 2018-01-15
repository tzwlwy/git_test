
from selenium import webdriver
import  time


dr = webdriver.Chrome("chromedriver.exe")
dr.get('https://www.baidu.com/')
time.sleep(1)
dr.close()
poem = '''
曾松，你好
'''
with open(r'D:\PHOTO\曾松点开看看.txt', 'wt') as fout:
   fout.write(poem)


