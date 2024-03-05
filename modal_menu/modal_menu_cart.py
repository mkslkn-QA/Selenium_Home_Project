'''
Всплывающее меню корзины
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ModalShoppingCartLocators:
    '''
    Локаторы всплывающей справа корзины
    '''
    SHOPPING_CART = (By.CSS_SELECTOR, 'div.modal-content [class*="button wc-forward"]')
    PLACE_ORDER = (By.CSS_SELECTOR, 'div.modal-content [class*="button checkout wc-forward"]')
    CLOSE = (By.CSS_SELECTOR, 'div.modal-header [class*="close-account"]')
    COUNTER_PLUS_ONE = (By.CSS_SELECTOR, 'div.modal-content [class*="increase"]')
    COUNTER_MINUS_ONE = (By.CSS_SELECTOR, 'div.modal-content [class*="decrease"]')
    DELETE = (By.CSS_SELECTOR, 'div.woocommerce-cart-item__qty [class="name"]')
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, 'div.modal-content [class*="button-larger"]')
    TEXT_EMPTY_CART = (By.CSS_SELECTOR, 'div.modal-content [class*="empty-message"]')

class ModalShoppingCart(BasePage):
    '''
    Методы для взаимодействия с всплывающим меню корзины товаров
    '''
    def go_to_shopping_cart_page(self):
        '''
        Переход на страницу карзины товаров
        '''
        self.find_element(ModalShoppingCartLocators.SHOPPING_CART).click()

    def go_to_place_order(self):
        '''
        Переход на страницу оформления товара
        '''
        self.find_element(ModalShoppingCartLocators.PLACE_ORDER).click()

    def close_shopping_cart_alert(self):
        '''
        Закрыть вспдывающую карзину товаров
        '''
        self.find_element(ModalShoppingCartLocators.CLOSE).click()

    def delete_from_modal_shopping_cart(self):
        '''
        Удалить из корзины
        '''
        WebDriverWait(self.driver, timeout=5, poll_frequency=1).until(
            EC.visibility_of_element_located((ModalShoppingCartLocators.DELETE)), message= f'Element not found!').click()

    

