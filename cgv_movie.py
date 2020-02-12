from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.request, time

url = 'http://www.cgv.co.kr/movies/'

# 크롬창 안띄우고 실행하는 옵션 추가
chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome('chromedriver', options = chrome_options)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

data_list = soup.select('#contents > div.wrap-movie-chart > div.sect-movie-chart > ol')

# print(data_list)

for data in data_list:
    for i in data.select('strong.title'):
        print(i.text)

    for i in data.select('strong.percent > span'):
        print(i.text)