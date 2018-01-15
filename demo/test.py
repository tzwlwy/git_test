
from selenium import webdriver
import  time


dr = webdriver.Chrome("chromedriver.exe")
dr.get('https://www.baidu.com/')
time.sleep(1)
dr.close()
poem = '''
testgit
'''
with open(r'D:\PHOTO\git_test.txt', 'wt') as fout:
   fout.write(poem)


