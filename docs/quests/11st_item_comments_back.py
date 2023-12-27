# 상품 : #thisClick_5649007961
# 상품 명칭 : 
# image link : 
# 원가 : 
# 판매가 : 
# 상품정보 : 

# 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# mongodb에 접속 -> database 연결 -> collection 작업
from pymongo import MongoClient
def Connect_Mongo():
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["gatheringdatas"]
    collection = database['11st_comments']
    collection.delete_many({})
    return collection

# webdriver 설치
webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행(Chrome 열기)
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력(https://www.w3schools.com/) 후 Enter
url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=11"
browser.get(url)

# 정보 획득
from selenium.webdriver.common.by import By

# 



element_article = browser.find_elements(by=By.CSS_SELECTOR, value="#thisClick_5649007961")
for article in element_article :
    article.click()
    time.sleep(1)
    element_title = browser.find_element(by=By.CSS_SELECTOR, value="div > h1")
    print("물건명 : {}".format(element_title.text))

    browser.back()
    time.sleep(1)
    pass
pass