# 몽고디비에서 컨테이너에 숫자가 있는경우 : 삭제 명령어 db.getCollection('요기에 컬랙션 이름 넣기').deleteMany({}) ;
# list : #review-list-page-area > ul > li
# 작성자 : dt.name
# ifrmReview 옵션 : #ifrmReview
# 별점 : p.grade > span > em
# 리뷰 내용 : div.cont_text_wrap
# 더보기 클릭 : #review-list-page-area > div > button

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
    collection = database['11st_comments']                        # collection 작업
    collection.delete_many({})
    return collection

# webdriver를 설치
webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행(Chrome 열기)
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력(https://www.w3schools.com/) 후 Enter
browser.get("https://www.11st.co.kr/products/6388266303?inpu=&trTypeCd=22&trCtgrNo=895019")

# - 가능 여부에 대한 OK 받음(selenium으로 대신한다.)
pass

# - html 파일 받음(and 확인)(selenium으로 대신한다.)
html = browser.page_source

# 정보 획득
from selenium.webdriver.common.by import By

# iframe 으로 전환
browser.switch_to.frame("ifrmReview")

# iframe 안에 있는 더보기를 전부 클릭 해준다. time sleep은 1초
while True :
    try :
        browser.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > div > button").click()
    except : 
        break
    time.sleep(1)
    pass

# 더보기 완료! -> 작성자, 별점 점수, 리뷰내용 찾기
def insert_db(collection):
    selector_value = "#review-list-page-area > ul > li"
    element_body = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
    for element_item in element_body :
        try :       # 작성자
            element_name = element_item.find_element(by=By.CSS_SELECTOR, value="dt.name")
            element_name = element_name.text
        except :
            element_name = "None"
            
        try :       # 별점 점수
            element_score = element_item.find_element(by=By.CSS_SELECTOR, value="p.grade > span > em")
            element_score = element_score.text
        except :
            element_score = "None"
            
        try :       # 리뷰내용
            element_review = element_item.find_element(by=By.CSS_SELECTOR, value="div.cont_text_wrap")
            element_review = element_review.text
        except :
            element_review = "None"

        collection.insert_one({"작성자": element_name, "별점 점수": element_score, "리뷰내용": element_review})     # insert 작업 진행
        pass

collection = Connect_Mongo()
insert_db(collection)

# 브라우저 종료
browser.quit()
