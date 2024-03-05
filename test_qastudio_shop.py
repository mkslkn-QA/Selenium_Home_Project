'''
Test case list
'''
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.favourites_page import FavoritesPage
from pages.order_page import OrderPage
from helper.input_helper import InputHelper
from pages.base_page import BasePage
from pages.product_page import ProductPage
from modal_menu.modal_menu_cart import ModalShoppingCart
from modal_menu.modal_menu_cart import ModalShoppingCartLocators
from pages.base_page import TMLocators

URL = 'https://testqastudio.me/'

@pytest.mark.smoke
class TestSmoke:
    """
    Basic tests
    """
    @pytest.mark.parametrize('key, value', [('[class*="11345"]', 'yith-wcwl-row-11345'),
                             ('[class*="11334"]', 'yith-wcwl-row-11334'),
                             ('[class*="11335"]', 'yith-wcwl-row-11335')]) 
    def test_add_in_favourite(self, browser, key, value):
        '''
        Test case #1
        Добавить в избранное
        '''
        main_page = BasePage(browser)
        main_page.go_to_site()
        main_page.go_to_element((By.CSS_SELECTOR, key))

        product_page = ProductPage(browser)
        product_page.add_to_favourites()
        product_page.go_to_favourites_page()

        WebDriverWait(browser, timeout=10, poll_frequency=2).until(
            EC.presence_of_element_located((By.ID, value)))

        assert product_page.get_current_url() == 'https://testqastudio.me/wishlist/'
        
    def test_delete_favourites(self, browser):
        '''
        Test case #2
        Удалить из избранного
        '''
        main_page = BasePage(browser)
        main_page.go_to_site()
        main_page.go_to_element((By. CSS_SELECTOR, '[class*="11341"]'))

        product_page = ProductPage(browser)
        product_page.add_to_favourites()
        product_page.go_to_favourites_page()

        favourites_page = FavoritesPage(browser)
        favourites_page.delete_from_favourites()

        assert favourites_page.alert_product_delete() == 'Продукт успешно удален из избранного'
                                          
    def test_buying_goods(self, browser):
        '''
        Test case #3
        Оформление заказа
        '''
        page = BasePage(browser)
        page.go_to_site()
        page.go_to_element((By.CSS_SELECTOR, '[class*="11328"]'))

        product_page = ProductPage(browser)
        product_page.add_in_shopping_cart()
        
        modal_menu = ModalShoppingCart(browser)
        modal_menu.go_to_place_order()

        order_page = InputHelper(browser)
        order_page.enter_input(input_id='billing_first_name', data='Ivan')
        order_page.enter_input(input_id='billing_last_name', data='Ivanov')
        order_page.enter_input(input_id='billing_address_1', data='11-1, Malaya Bronnaya')
        order_page.enter_input(input_id='billing_city', data='Moscow')
        order_page.enter_input(input_id='billing_state', data='Moscow')
        order_page.enter_input(input_id='billing_postcode', data='81346')
        order_page.enter_input(input_id='billing_phone', data='+79999677895')
        order_page.enter_input(input_id='billing_email', data='random@gmail.com')
        order_page = OrderPage(browser)
        order_page.press_button_confirm_order()

        WebDriverWait(browser, timeout=5, poll_frequency=1).until(
            EC.url_contains("https://testqastudio.me/checkout/order-received/"))

        result = WebDriverWait(browser, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Ваш заказ принят. Благодарим вас."))

        assert result, 'Unexpected notification text'

    def test_delete_from_modal_shopping_cart(self, browser):
        '''
        Test case #4
        Удалить товар из корзины
        '''
        main_page = BasePage(browser)
        main_page.go_to_site()
        main_page.go_to_element((By.CSS_SELECTOR, '[class*="11337"]'))

        product_page = ProductPage(browser)
        product_page.add_in_shopping_cart()
        product_page = ModalShoppingCart(browser)
        product_page.delete_from_modal_shopping_cart()

        WebDriverWait(browser, timeout=5, poll_frequency=1).until(EC.text_to_be_present_in_element(
            (ModalShoppingCartLocators.TEXT_EMPTY_CART), 'Ваша корзина пуста'))
        
        assert WebDriverWait(browser, timeout=5, poll_frequency=1).until(EC.element_to_be_clickable(
            (ModalShoppingCartLocators.CONTINUE_SHOPPING)))


    def test_add_to_shopping_cart(self, browser):
        '''
        Test case #5
        Добавить товар в корзину и перейти на страницу корзины
        '''
        page = BasePage(browser)
        page.go_to_site()
        page.go_to_element((By.CSS_SELECTOR, '[class*="11343"]'))
        product_page = page
        product_page = ProductPage(browser)
        product_page.add_in_shopping_cart()

        WebDriverWait(browser, timeout=10, poll_frequency=2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[class*="11343"]')))
        
        product_page = ModalShoppingCart(browser)
        product_page.go_to_shopping_cart_page()

        assert product_page.get_current_url() == 'https://testqastudio.me/cart/'



        

        


        


        

        
        


        

       