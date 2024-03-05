'''
Локаторы страницы "Избранное"
'''
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FavouritesLocators:
    '''
    Локаторы страницы
    '''
    DELETE = (By.CSS_SELECTOR, 'td.product-remove [class*=remove]')
    ALERT = (By.CSS_SELECTOR, '[class*="woocommerce-message"]')
    IN_CART = (By.CSS_SELECTOR, 'td.product-add-to-cart [class*="wp-element-button"]')

class FavoritesPage(BasePage):
    '''
    Страница избранное
    '''        
    def delete_from_favourites(self):
        '''
        Удалить из избранного
        '''
        self.find_element(FavouritesLocators.DELETE).click()

    def alert_product_delete(self):
        '''
        Алерт всплывающий после удаления товара
        '''
        alert = self.find_element(FavouritesLocators.ALERT)
        return alert.text


