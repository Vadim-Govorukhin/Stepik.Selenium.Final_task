from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket_page(self):
        btn = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        btn.click()
        
        self.solve_quiz_and_get_code()
    
    def should_be_added_to_basket(self):
        product_name, product_price = self.should_be_name_and_price()
        
        self.should_be_name_after_addition(product_name)
        self.should_be_matching_price(product_price)
    
    def should_be_name_and_price(self,):
        product_area = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_PRICE)
        product_info = product_area.text
        product_name, product_price = product_info.split('\n')[:2]
        return product_name, product_price
    
    def should_be_name_after_addition(self, product_name):
        text_area = self.browser.find_element(*ProductPageLocators.BOOK_ADDED_NAME)
        assert product_name == text_area.text, "Difference between name of product and added to basket product"
        print('Name check: OK')
        
    def should_be_matching_price(self, product_price):
        basket_price_area = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert product_price in basket_price_area.text, "Price of product not equals price of basket"
        print('Price check: OK')
                