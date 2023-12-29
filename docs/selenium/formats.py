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
browser.get("https://www.w3schools.com/")                          # 크롬 브라우저에 주소 넣는거와 같음.

# - 가능 여부에 대한 OK 받음(selenium으로 대신한다.)
pass
# - html 파일 받음(and 확인)(selenium으로 대신한다.)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By

pass
# browser.save_screenshot('./formats.png')                            # 진행된 결과 스크린샷을 저장해준다.

# 브라우저 종료
browser.quit()


