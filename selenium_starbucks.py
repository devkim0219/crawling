from selenium import webdriver
from bs4 import BeautifulSoup
import time, requests
from selenium.webdriver.chrome.options import Options

# 크롬창 안띄우고 실행하는 옵션 추가
chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome('chromedriver', options = chrome_options)

starbucks = driver.get('http://www.istarbucks.co.kr/store/store_map.do')
time.sleep(3)

loca = driver.find_element_by_class_name('loca_search')
loca.click()
time.sleep(1)

sido = driver.find_element_by_class_name('sido_arae_box')
li = sido.find_elements_by_tag_name('li')
li[5].click()
time.sleep(1)

gugun = driver.find_element_by_class_name('gugun_arae_box')
li = gugun.find_elements_by_tag_name('li')
li[-1].click()
time.sleep(1)

source = driver.page_source

bs = BeautifulSoup(source, 'lxml')

entire = bs.find('ul', class_ = 'quickSearchResultBoxSidoGugun')

li_list = entire.find_all('li')

for li in li_list:
    print(li.find('p').text)

driver.close()