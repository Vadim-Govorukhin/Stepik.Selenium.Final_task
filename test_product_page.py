from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    
    basket = BasketPage(browser, browser.current_url)
    basket.should_not_be_products()
    basket.should_be_empty_message()

@pytest.mark.skip(reason="no need of testing this")
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip(reason="no need of testing this") 
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    
@pytest.mark.parametrize('promo', ["?promo=offer0",
                                  "?promo=offer1",
                                  "?promo=offer2",
                                  "?promo=offer3",
                                  "?promo=offer4",
                                  "?promo=offer5",
                                  "?promo=offer6",
                                  pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                  "?promo=offer8",
                                  "?promo=offer9"])
@pytest.mark.skip(reason="no need of testing this")
def test_guest_can_add_product_to_basket(browser, promo):
    #link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}'
    print(f'--------- {promo}')
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.add_to_basket_page()
    page.solve_quiz_and_get_code()
    
    page.should_be_added_to_basket()
    
@pytest.mark.skip(reason="no need of testing this")    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    
    page.add_to_basket_page()    
    page.should_not_be_success_message()
        
@pytest.mark.skip(reason="no need of testing this")
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    
    page.should_not_be_success_message()
    
@pytest.mark.skip(reason="no need of testing this")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    
    page.add_to_basket_page()    
    page.should_be_disappeared_success_message()
    