# * 웹 크롤링 동작
from selenium import webdriver

# ChromeDriver 실행
browser = webdriver.Chrome("../ChromeDriver.exe")

# Chrome WebDriver의 capabilities 속성 사용
# capabilities = browser.capabilities

# - 주소에 https://www.w3schools.com/ 입력
browser.get("https://www.w3schools.com/")                   # 크롬 브라우저에 주소 넣는거와 같음.

# - 가능 여부에 대한 ok 사인
pass
# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

# - 정보 획득
pass
# 브라우저 종료
browser.quit()


