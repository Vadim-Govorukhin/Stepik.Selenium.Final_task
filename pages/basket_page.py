from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_not_be_products(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
           "Basket is not empty, but should be"
           
    def should_be_empty_message(self):
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty.",}
        text_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
        
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        assert languages[language] in text_message, \
            "Massage of empty basket is wrong"