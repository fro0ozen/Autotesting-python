import pytest
import logging
from base import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.segments_page import SegmentsPage
import os


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def dashboard_page(driver):
    return DashboardPage(driver=driver)


@pytest.fixture
def segments_page(driver):
    return SegmentsPage(driver=driver)


def get_driver():
    options = Options()
    manager = ChromeDriverManager(version='latest', log_level=logging.CRITICAL)
    browser = webdriver.Chrome(executable_path=manager.install(), options=options)

    browser.maximize_window()
    return browser


@pytest.fixture(scope='function')
def driver(config, temp_dir):
    url = "https://target.my.com/"
    browser = get_driver()
    browser.get(url)

    yield browser
    browser.quit()

@pytest.fixture()
def file_path(repo_root):
    return os.path.join(repo_root, 'files', 'banner_image.jpg')
