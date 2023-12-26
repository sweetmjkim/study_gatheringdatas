# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력(https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033) 후 Enter
browser.get("https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033")                          # 크롬 브라우저에 주소 넣는거와 같음.

# - 가능 여부에 대한 OK 받음
pass


# 해당 진행시 참고 자료
# 전체 : div.mnemitem_unit
# #swiper-wrapper-7c273d0b5e1476ed > li.mnemitem_grid_item.swiper-slide.swiper-slide-next > div

# brand : span.mnemitem_goods_brand
# #swiper-wrapper-7c273d0b5e1476ed > li.mnemitem_grid_item.swiper-slide.swiper-slide-next > div > a > div.mnemitem_tit > span.mnemitem_goods_brand

# title : span.mnemitem_goods_tit
# #swiper-wrapper-7c273d0b5e1476ed > li:nth-child(1) > div > a > div.mnemitem_tit > span.mnemitem_goods_tit

# old_price : div > del > em
# #swiper-wrapper-7c273d0b5e1476ed > li.mnemitem_grid_item.swiper-slide.swiper-slide-next > div > a > div.mnemitem_pricewrap_v2 > div.mnemitem_price_row.ty_oldpr > div > del > em



# - 정보 획득
from selenium.webdriver.common.by import By
selector_value = "div.mnemitem_unit"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)

for element_item in element_bundle[10:31] :     #list slicing 기법
    # print(element_item.text)      # 상품 정보들
    # 상품 제목
    element_title = element_item.find_element(by=By.CSS_SELECTOR, value="span.mnemitem_goods_tit")
    title = element_title.text
    # 상품 판매 원가 (try~except 포함)
    try : 
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value="div > del > em")
        old_price = element_old_price.text
        pass
    except : 
        old_price = ""
        pass
    finally :
        pass
    
    print("title : {}, old price : {}".format(title, old_price))
    pass
pass

# 브라우저 종료
browser.quit()


