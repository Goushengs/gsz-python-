from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(r"D:\pythontest\venv\Scripts\chromedrivers.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://www.baidu.com')
# driver.close()
