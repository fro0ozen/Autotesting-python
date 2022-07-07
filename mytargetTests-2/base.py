import pytest
import os
import allure
import datetime
import random
import faker
from _pytest.fixtures import FixtureRequest
from ui.pages.main_page import MainPage
from ui.pages.dashboard_page import DashboardPage

CLICK_RETRY = 3


class BaseCase:

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_tests_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_tests_count:
            screenshot = os.path.join(temp_dir, 'failure.png')
            driver.get_screenshot_as_file(screenshot)
            allure.attach.file(screenshot, 'failure.png', attachment_type=allure.attachment_type.PNG)

            browser_log = os.path.join(temp_dir, 'browser.log')
            with open(browser_log, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")

            with open(browser_log, 'r') as f:
                allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.logger = logger
        self.main_page: MainPage = request.getfixturevalue('main_page')

    @pytest.fixture(scope="function")
    def login_fixture(self):
        self.main_page.login()
        return DashboardPage(self.main_page.driver)

    @pytest.fixture(scope="function")
    def _name_generator(self):
        return faker.Faker().bothify(text='???????-???????-#######')

    @pytest.fixture(scope="function")
    def dashboard_fixture(self, _name_generator, login_fixture):
        name = _name_generator
        return name, login_fixture

    @pytest.fixture(scope="function")
    def new_segment(self, dashboard_fixture):
        name, dashboard_page = dashboard_fixture
        segment_page = dashboard_page.go_to_segments(dashboard_page.locators.AUDITORY_LOCATOR)
        locator = segment_page.create_new_segment(name)
        return name, locator, segment_page
