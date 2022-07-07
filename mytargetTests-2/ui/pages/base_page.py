import logging
import time

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.static_variables import CLICK_RETRY, BASE_TIMEOUT


class PageNotLoadedException(Exception):
    pass


# Базовая страница
class BasePage(object):
    url = ''
    locators = None

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger("test")
        self.is_opened()

    def is_opened(self, timeout=BASE_TIMEOUT):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True

        raise PageNotLoadedException(f'{self.url} did not open in {timeout}sec for {self.__class__.__name__}.\n'
                                     f'Current url: {self.driver.current_url}.')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        self.logger.debug(f"Click on {locator}")

        for i in range(CLICK_RETRY):
            try:
                self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                self.scroll_to(elem)
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY-1:
                    raise

    def check_visibility(self, locator, timeout=None, visible=True):
        try:
            if visible:
                self.logger.debug(f"Is {locator} visible")

                self.wait(timeout=timeout).until(EC.visibility_of_element_located(locator))
            else:
                self.logger.debug(f"Is {locator} invisible")

                self.wait(timeout=timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def clear_and_send_keys(self, locator, data, timeout=None):
        self.logger.debug(f"Send {data} to {locator}")

        input_field = self.find(locator, timeout=timeout)
        input_field.clear()
        input_field.send_keys(data)
