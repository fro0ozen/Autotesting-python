import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(scope='function')
def driver():

    options = Options()
    manager = ChromeDriverManager(version='latest')
    browser = webdriver.Chrome(executable_path=manager.install(), options=options)
    browser.maximize_window() #необходимо, чтобы все центральное меню было видно на экране
    browser.get('https://target.my.com')
    yield browser
    browser.close()
