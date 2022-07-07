from ui.locators.basic_locators import MainPageLocators
from ui.pages.base_page import BasePage
import ui.pages.static_variables
import allure


# Начальная страница
class MainPage(BasePage):
    url = 'https://target.my.com/'
    locators = MainPageLocators()

    @allure.step("Login")
    def login(self, email=ui.pages.static_variables.login_email, password=ui.pages.static_variables.login_password):
        self.logger.info("Login")

        self.click(self.locators.ENTER_BUTTON_LOCATOR)
        self.clear_and_send_keys(self.locators.ENTER_EMAIL_LOCATOR, email)
        self.clear_and_send_keys(self.locators.ENTER_PASSWORD_LOCATOR, password)
        self.click(self.locators.ENTER_LOCATOR)
