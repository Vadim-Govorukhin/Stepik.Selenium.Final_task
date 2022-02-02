from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_BASKET_BTN = (By.CSS_SELECTOR, ".basket-mini .btn-group a.btn-default")

class BasketPageLocators:
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#content_inner")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")
                      
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
                  
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
                     
class ProductPageLocators:                     
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_PRICE = (By.CSS_SELECTOR, ".product_main")
    BOOK_ADDED_NAME = (By.CSS_SELECTOR, "div.alert-success strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner p")
    
    
    
    
    