from selenium import webdriver

# - chrome browser 열기
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriver 업데이트
webdriver_manager = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

pass