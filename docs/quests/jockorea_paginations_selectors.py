# * 웹 크롤링 동작
# (install browser)
# setup driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.chrome.options import Options

# Chrome 브라우저 옵션 생성
chrome_options = Options()

# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행(Chrome 열기)
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory), options=chrome_options)

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력(https://www.w3schools.com/) 후 Enter

# for page_number in [1,2,3,4,5,6,7] :        # page number
for page_number in range(1,11) :        # page number
    url = "https://www.coupang.com/np/campaigns/348?page=".format(page_number)
    browser.get(url)
    time.sleep(3)
    # - html 파일 받음(and 확인)(selenium으로 대신한다.)
    html = browser.page_source
    pass

# - 가능 여부에 대한 OK 받음(selenium으로 대신한다.)
pass
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By

pass
# browser.save_screenshot('./formats.png')

# 브라우저 종료
browser.quit()