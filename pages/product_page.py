from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_basket_page(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        link.click()
        
        self.solve_quiz_and_get_code()
        
    