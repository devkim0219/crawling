from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

url = "https://pjt3591oo.github.io/search"

#webdriver 설정                    
# driver = webdriver.Chrome('./chromedriver.exe') 
driver = webdriver.Chrome('chromedriver')

driver.get(url)

# selected_tag_a = driver.find_element_by_css_selector('input#search-box')

# selected_tag_a.click()

# selected_tag_a.send_keys('test')
# selected_tag_a.send_keys(Keys.ENTER)

# driver.execute_script('alert("test")')

# soup = BeautifulSoup(driver.page_source)

# 크롬 브라우저 내부대기
# browser.implicitly_wait(5)

# 속성 확인
# print(dir(browser))

# 브라우저 사이즈
# browser.set_window_size(1920,1280) #maxmize_window(), minimize_window()

# 페이지 이동
# browser.get("http://www.daum.net")

# 페이지 내용
# print('page contents : {}'.format(browser.page_source))

# 검색창 input 선택
# element = browser.find_element_by_css_selector('div.inner_search > input.tf_keyword')

# 검색어 입력
# element.send_keys('테스트 검색')

# 검색(Form Submit)
# element.submit()

# 스크린샷 저장1
# browser.save_screenshot("c:/website_ch1.png")

# 스크린샷 저장2
# browser.get_screenshot_as_file("c:/website_ch2.png")

# 브라우저 종료
# browser.quit()