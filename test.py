
from selenium import webdriver
import  time


dr = webdriver.Chrome("chromedriver.exe")
dr.get('https://www.baidu.com/')

time.sleep(3)
