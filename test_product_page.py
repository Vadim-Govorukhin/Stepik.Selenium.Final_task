from pages.product_page import ProductPage
import pytest

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
def test_guest_can_add_product_to_basket(browser, promo):
    #link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}'
    print(f'--------- {promo}')
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.add_to_basket_page()
    
    page.should_be_added_to_basket()
    