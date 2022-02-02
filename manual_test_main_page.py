from selenium import webdriver
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
link = "http://selenium1py.pythonanywhere.com/"
browser.get(link)
button = browser.find_element_by_css_selector(".basket-mini .btn-group a.btn-default")
button.click()

text = browser.find_element_by_css_selector("#content_inner")

#SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
#is_disappeared(SUCCESS_MESSAGE)