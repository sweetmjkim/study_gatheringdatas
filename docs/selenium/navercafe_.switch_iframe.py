# * 웹 크롤링 동작
# (install browser)
# setup driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행(Chrome 열기)
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력(https://www.w3schools.com/) 후 Enter
browser.get("https://cafe.naver.com/peopledisc")

# - 가능 여부에 대한 OK 받음(selenium으로 대신한다.)
pass
# - html 파일 받음(and 확인)(selenium으로 대신한다.)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
# 병원 진료 후기 메뉴 클릭
# browser.find_element(by=By.css_SELECTOR, value="#menuLink84").click()
element_click = browser.find_element(by=By.CSS_SELECTOR, value="#menuLink84")
element_click.click()

# iframe 으로 전환
browser.switch_to.frame("cafe_main")


#main-area > div:nth-child(4) > table > tbody >tr : 해당 리스트
cafe_list = browser.find_elements(by=By.CSS_SELECTOR, value="#main-area > div:nth-child(4) > table > tbody >tr")
pass

# 브라우저 종료
browser.quit()


