# list : div.css-13j4ly.egj9y8a4
# 작성자 : div.css-eldyae.e10cf2lr1
# 별점 점수 : div.css-31ods0.egj9y8a0 > span
# 내용 : div.css-2occzs.egj9y8a1

# * 웹 크롤링 동작
# (install browser)
# setup driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

from pymongo import MongoClient
def Connect_Mongo():
    mongoClient = MongoClient("mongodb://localhost:27017")          # mongodb에 접속
    database = mongoClient["gatheringdatas"]                        # database 연결
    collection = database['watcha_comments']                        # collection 작업
    collection.delete_many({})
    return collection

# 크롬 드라이브를 설치해서 크롬 드라이브의 위치를 쉽게 찾아주는 역할
webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행(Chrome 열기)
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력(https://www.w3schools.com/) 후 Enter
browser.get("https://pedia.watcha.com/ko-KR/contents/m5NnBep/comments")

# - 가능 여부에 대한 OK 받음(selenium으로 대신한다.)
pass
# - html 파일 받음(and 확인)(selenium으로 대신한다.)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
## 한 페이지씩 이동
element_body = browser.find_element(by=By.CSS_SELECTOR, value="body")

previous_scrollHeight = 0
while True :
    element_body.send_keys(Keys.END)

    current_scrollHeight = browser.execute_script("return document.body.scrollHeight")
    if previous_scrollHeight >= current_scrollHeight :
        break
    else : 
        previous_scrollHeight = current_scrollHeight
    time.sleep(3)
    pass

def insert_db(collection):
    selector_value = "div.css-13j4ly.egj9y8a4"
    element_body = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
    for element_item in element_body :
        try :       # 작성자
            element_name = element_item.find_element(by=By.CSS_SELECTOR, value="div.css-eldyae.e10cf2lr1")
            element_name = element_name.text
        except :
            element_name = "None"
            
        try :       # 별점 점수
            element_score = element_item.find_element(by=By.CSS_SELECTOR, value="div.css-31ods0.egj9y8a0 > span")
            element_score = element_score.text
        except :
            element_score = "None"
            
        try :       # 리뷰내용
            element_review = element_item.find_element(by=By.CSS_SELECTOR, value="div.css-2occzs.egj9y8a1")
            element_review = element_review.text
        except :
            element_review = "None"

        collection.insert_one({"작성자": element_name, "별점 점수": element_score, "리뷰내용": element_review})     # insert 작업 진행
        pass

collection = Connect_Mongo()
insert_db(collection)

# 브라우저 종료
browser.quit()



