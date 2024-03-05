'''
страница товара
'''
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPageLocators:
    '''
    Локаторы для страницы продукта
    '''
    FAVOURITES = (By.CSS_SELECTOR, 'div.product-button-wrapper [class*="add-to-wishlist"]')
    IN_SHOPPING_CART = (By.CSS_SELECTOR, 'div.site-content [name="add-to-cart"]')
    COUNTER_PLUS = (By.CSS_SELECTOR, 'div.site-content [class*="increase"]')
    COUNTER_MINUS = (By.CSS_SELECTOR, 'div.site-content [class*="decrease"]')
    SKU = (By.CSS_SELECTOR, 'span.sku_wrapper [class="sku"]')

class ProductPage(BasePage):
    '''
    Базовые методы для раборты со страницей товара
    '''        
    def add_to_favourites(self):
        '''
        Добавить товар в избранное
        '''
        self.find_element(ProductPageLocators.FAVOURITES).click()
        WebDriverWait(self.driver, timeout=5, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="yith-wcwl-wishlistaddedbrowse"]')), message= f'Element not found!')


    def add_in_shopping_cart(self):
        '''
        Добавить товар в корзину
        '''
        self.find_element(ProductPageLocators.IN_SHOPPING_CART).click()

    