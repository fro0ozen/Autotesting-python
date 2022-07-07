import pytest
import creds
from ui.locators import basic_locators
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException,\
                                        ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CLICK_RETRY = 3


class BaseCase:

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 4
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                self.find(locator, timeout=timeout)
                self.wait(timeout).until(EC.element_to_be_clickable(locator)).click()
                return
            except (StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException):
                if i == CLICK_RETRY-1:
                    raise

    @pytest.fixture(scope='function')
    def login(self):
        self.click(basic_locators.ENTER_BUTTON_LOCATOR)
        email = self.find(basic_locators.ENTER_EMAIL_LOCATOR)
        email.clear()
        email.send_keys(creds.login_email)
        password = self.find(basic_locators.ENTER_PASSWORD_LOCATOR)
        password.clear()
        password.send_keys(creds.login_password)
        self.click(basic_locators.ENTER_LOCATOR)

    def send_keys(self, locator, data):
        input_field = self.find(locator)
        input_field.clear()
        input_field.send_keys(data)

    def check_visibility(self, locator, timeout=None):
        try:
            self.wait(timeout=timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
