
from selenium import webdriver
import  time


dr = webdriver.Chrome("chromedriver.exe")
dr.get('https://www.baidu.com/')
time.sleep(1)
dr.close()
poem = '''
test
'''
with open('data_list.txt', 'wt') as fout:
   fout.write(poem)




