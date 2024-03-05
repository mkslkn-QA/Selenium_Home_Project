'''
Страница оформления заказа
'''

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderPageLocators:
    '''
    Локаторы страницы заказа
    '''
    BUTTON_CONFIRM_ORDER = (By.ID, 'place_order')

class OrderPage(BasePage):
    '''
    Базовые методы для работы со страницей заказа
    '''
    def press_button_confirm_order(self):
        '''
        Нажать кнопку "оформить заказ"
        '''
        self.find_element(OrderPageLocators.BUTTON_CONFIRM_ORDER).click()


    
    
    
