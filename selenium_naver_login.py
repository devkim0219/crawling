from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://nid.naver.com/nidlogin.login')

id = 'ssalbae1986'
pw = '@tkdekatk0217'

driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[1]/a').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="login_maintain"]/span[1]').click()
time.sleep(1)

# 브라우저등록 화면 처리
driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/form/fieldset/span[1]/a').click()
time.sleep(1)

# 네이버 페이 들어가기
driver.get('https://order.pay.naver.com/home')
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

notices = soup.select('div.p_inr > div.p_info > a > span')
point = soup.select_one('.my_npoint strong')
print(point.string)

time.sleep(5)
driver.close()