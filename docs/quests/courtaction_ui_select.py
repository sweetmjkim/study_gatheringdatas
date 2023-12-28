# * 웹 크롤링 동작
# (install browser)
# setup driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# mongodb에 접속 -> database 연결 -> collection 작업
from pymongo import MongoClient
def Connect_Mongo():
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["gatheringdatas"]
    collection = database['courtauction']
    collection.delete_many({})
    return collection

# webdriver를 설치
webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행(Chrome 열기)
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력 후 Enter
browser.get("https://www.courtauction.go.kr/")

# iframe 으로 전환
browser.switch_to.frame('indexFrame')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# 사이트 접속 -> 경매물건 클릭 -> 법원/소재지(서울서부지방법원) -> 검색 클릭 -> 법원소재지, 사건번호, 소재지및내역 DB저장 -> 이전 클릭
# -> 법원/소재지 ~ 이전 클릭 2번 반복 -> 브라우저 종료

# 메인 화면 상단 경매물건 메뉴 클릭
browser.find_element(by=By.CSS_SELECTOR, value="#menu > h1:nth-child(5) > a > img").click()

selector_value = "#contents > div.table_contents"
# 법원/소재지 리스트 : #idJiwonNm > option
element_courts = browser.find_elements(by=By.CSS_SELECTOR, value="#idJiwonNm > option")

from selenium.webdriver.support.ui import Select
def insert_db(collection) :
    for index in range(len(element_courts)) :
        element_courtauction = Select(browser.find_element(by=By.CSS_SELECTOR, value="#idJiwonNm"))
        element_courtauction.select_by_index(index)
           # 물건상세검색 페이지에서 검색버튼 클릭
        url = "#contents > form > div.tbl_btn > a:nth-child(1) > img"
        browser.find_element(by=By.CSS_SELECTOR, value=url).click()
        time.sleep(1)
        for element_index in range(len(element_courtauction.options)) :
            try :       # 법원소재지
                element_law_location = element_courtauction.options[element_index].find_element(by=By.CSS_SELECTOR, value="search_title > ul > li:nth-child(1)")
                element_law_location = element_law_location.text
            except :
                element_law_location = "None"
                
            try :       # 사건번호
                element_event_number = element_courtauction.options[element_index].find_element(by=By.CSS_SELECTOR, value="form:nth-child(1) > table > tbody > tr:nth-child({}) > td:nth-child(2)".format())
                element_event_number = element_event_number.text
            except :
                element_event_number = "None"
                
            try :       # 소재지 및 내역
                element_location = element_courtauction.options[element_index].find_element(by=By.CSS_SELECTOR, value="table > tbody > tr:nth-child({}) > td:nth-child(4)".format())
                element_location = element_location.text
            except :
                element_location = "None"

            collection.insert_one({"법원소재지": element_law_location, "사건번호": element_event_number, "소재지 및 내역": element_location})
            pass
        url = "#contents > div.table_contents > form:nth-child(1) > div > div > a:nth-child(5) > img"
        browser.find_element(by=By.CSS_SELECTOR, value=url).click()
        time.sleep(3)
    
    # 물건상세검색 페이지에서 검색버튼 클릭
    url = "#contents > form > div.tbl_btn > a:nth-child(1) > img"
    browser.find_element(by=By.CSS_SELECTOR, value=url).click()
    time.sleep(1)

    # 이전 화면 : #contents > div.table_contents > form:nth-child(1) > div > div > a:nth-child(5) > img
    url = "#contents > div.table_contents > form:nth-child(1) > div > div > a:nth-child(5) > img"
    browser.find_element(by=By.CSS_SELECTOR, value=url).click()
    time.sleep(3)
    pass
pass
collection = Connect_Mongo()
insert_db(collection)
# 브라우저 종료
browser.quit()

