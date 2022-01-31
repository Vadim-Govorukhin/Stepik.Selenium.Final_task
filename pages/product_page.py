from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket_page(self):
        btn = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        btn.click()
        
        self.solve_quiz_and_get_code()
    
    def should_be_added_to_basket(self):
        product_area = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_PRICE)
        product_info = product_area.text
        product_name, product_price = product_info.split('\n')[:2]
        
        self.should_be_name_after_addition(product_name)
        self.should_be_matching_price(product_price)
        
    def should_be_name_after_addition(self, product_name):
        text_area = self.browser.find_element(*ProductPageLocators.TEXT_AFTER_ADD)
        assert product_name in text_area.text, "No name of product after addition to basket"
        print('Name check: OK')
        
    def should_be_matching_price(self, product_price):
        basket_price_area = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert product_price in basket_price_area.text, "Price of product not equals price of basket"
        print('Price check: OK')
                