import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')

def browser():
    chrome_options = Options()
    chrome_options.add_argument('start_maximized')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extentions')
    chrome_options.add_argument('--disable-application-cache')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-setuid-sandbox')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    chrome_options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    driver_path = "C:\\chromedriver-win64\\chromedriver.exe"

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()