'''
Input helper
'''
from selenium.webdriver.common.by import By
import time

class InputHelper:
    '''
    Методы для работы со страницей оформления заказа
    '''
    def __init__(self, driver):
        self.driver = driver

    def enter_input(self, input_id, data):
        ''' 
        Метод заполнения поля ввода
        '''
        input_field = self.driver.find_element(By.ID, value=input_id)
        input_field.click()
        input_field.send_keys(data)
        time.sleep(1)
        return input_field