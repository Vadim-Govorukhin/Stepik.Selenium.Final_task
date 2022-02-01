from selenium import webdriver
import math
from selenium.common.exceptions import NoAlertPresentException

browser = webdriver.Chrome()
promo = "?promo=offer6"
link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}'
browser.get(link)
button = browser.find_element_by_css_selector("button.btn-add-to-basket")
button.click()


def solve_quiz_and_get_code(browser):
    alert = browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")
        
solve_quiz_and_get_code(browser) 

text_area = browser.find_element_by_css_selector("div.alert-success strong")

name = browser.find_element_by_css_selector("div.alertinner p")
