from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# MongDB에 연결
from pymongo import MongoClient
def connect_Mongo() :
    MongoClient = MongoClient("mongodb://localhost:27017")
    database = MongoClient["gatheringdatas"]
    collection = database['watcha_comments']
    collection.delete_many({})
    return collection

# 크롬 드라이브를 설치해서 크롬 드라이브의 위치를 쉽게 찾아주는 역할
webdriver_manager_directory = ChromeDriverManager().install()

# chromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# 주소입력
browser.get("https://pedia.watcha.com/ko-KR/contents/m5NnBep/comments")

# - 가능 여부에 대한 OK 받음(selenium으로 대신한다.)
pass

# - html 파일 받음(and 확인)(selenium으로 대신한다.)
html = browser.page_source

# -정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 한 페이지씩 이동
element_body = browser.find_element(by=By.CSS_SELECTOR, value="body")

previous_scrollHeight = 0





# 브라우저 종료
browser.quit()