# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력(https://www.coupang.com/np/categories/184060) 후 Enter
browser.get("https://www.coupang.com/np/categories/184060")                          # 크롬 브라우저에 주소 넣는거와 같음.

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

# - 정보 획득
from selenium.webdriver.common.by import By

# ## 하나에 element 가져오기
# selector_value = "#\37 323106802 > a > dl > dd > div.name"
# element_path = browser.find_element(by=By.CSS_SELECTOR, value=selector_value)
# pass

## 여러개 elements 정보 가져오기                                                        # 상품명을 찾아줘
selector_value = "div.name"
elements_path = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
for webelements in elements_path :
    title = webelements.text
    print("{}".format(title))
    pass
pass

# 브라우저 종료
browser.quit()