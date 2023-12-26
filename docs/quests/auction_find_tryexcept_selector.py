# 상품제목, 판매원가, 변경가격, 배송방법(list)
# 고유 : github, 사용한 각각 element

# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력(https://corners.auction.co.kr/corner/categorybest.aspx) 후 Enter
browser.get("https://corners.auction.co.kr/corner/categorybest.aspx")

# - 가능 여부에 대한 OK 받음
pass

# - 정보 획득
from selenium.webdriver.common.by import By
selector_value = "div.img-list"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)

for element_item in element_bundle[0:31] :
    # 상품 제목
    selector_value_title = "em > a"
    element_title = element_item.find_element(by=By.CSS_SELECTOR, value="em > a")
    title = element_title.text
    
    # 판매 원가
    try :
        selector_value_old_price = "li.c_price"
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value = selector_value_old_price)
        old_price = "element_old_price"
        pass
    except :
        old_price = ""
        pass
    
    # 변경 가격
    try :
        selector_value_nwe_price = "li.d_price"
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value = selector_value_nwe_price)
        new_price = "element_new_price"
        pass
    except :
        new_price = ""
        pass
    
    # 배송 방법
    try :
        selector_value_delivery = "li.d_price"
        element_delivery = element_item.find_element(by=By.CSS_SELECTOR, value = selector_value_delivery)
        delivery = [list_element_delivery.text for list_element_delivery in element_delivery]
        pass
    except :
        delivery = ""
        pass
    
    print("title : {}, old price : {}, price : {}, delivery : {}".format(title, old_price, new_price, delivery))
    pass
pass

# 브라우저 종료
browser.quit()