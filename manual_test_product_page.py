from selenium import webdriver
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
promo = "?promo=offer6"
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
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
        
#solve_quiz_and_get_code(browser) 

#text_area = browser.find_element_by_css_selector("div.alert-success strong")

#name = browser.find_element_by_css_selector("div.alertinner p")

def is_disappeared(self, how, what, timeout=4):
    try:
        WebDriverWait(self.browser, timeout, 1, TimeoutException).\
            until_not(EC.presence_of_element_located((how, what)))
    except TimeoutException:
        return False
    return True

SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
is_disappeared(SUCCESS_MESSAGE)