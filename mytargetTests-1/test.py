from base import BaseCase
from ui.locators import basic_locators
import pytest


@pytest.mark.usefixtures("login")
class TestOne(BaseCase):

    # Тест на login
    @pytest.mark.UI
    def test_login(self):
        assert self.check_visibility(basic_locators.COMPANY_ACTIVATED_LOCATOR)

    # Тест на logout
    @pytest.mark.UI
    def test_logout(self):
        self.click(basic_locators.EXIT_MENU_LOCATOR, timeout=5)
        self.click(basic_locators.EXIT_BUTTON_LOCATOR, timeout=5)
        assert self.check_visibility(basic_locators.TITLE_LOCATOR)

    # Тест на изменение данных профиля
    @pytest.mark.UI
    def test_profile(self):
        self.click(basic_locators.PROFILE_LOCATOR)
        assert "https://target.my.com/profile" in self.driver.current_url
        name = "Иванов Иван Иванови"
        phone_number = "87777777777"
        self.send_keys(basic_locators.PROFILE_NAME_LOCATOR, name)
        self.send_keys(basic_locators.PROFILE_NUMBER_LOCATOR, phone_number)
        self.click(basic_locators.PROFILE_SAVE_BUTTON_LOCATOR)
        assert self.check_visibility(basic_locators.SUCCESS_SAVE_LOCATOR)

    @pytest.mark.parametrize(
        'page, link',
        [
            pytest.param(
                basic_locators.PAGE_COMPANY_LOCATOR,
                basic_locators.COMPANY_ACTIVATED_LOCATOR
            ),
            pytest.param(
                basic_locators.PAGE_AUDIENCE_LOCATOR,
                basic_locators.PAGE_AUDIENCE_ACTIVATED_LOCATOR
            ),
            pytest.param(
                basic_locators.PAGE_BALANCE_LOCATOR,
                basic_locators.PAGE_BALANCE_ACTIVATED_LOCATOR
            ),
            pytest.param(
                basic_locators.PAGE_STATISTIC_LOCATOR,
                basic_locators.PAGE_STATISTIC_ACTIVATED_LOCATOR
            ),
            pytest.param(
                basic_locators.PAGE_TOOLS_LOCATOR,
                basic_locators.PAGE_TOOLS_ACTIVATED_LOCATOR
            )
        ]
    )
    # Тестим центральное меню
    @pytest.mark.UI
    def test_pages(self, page, link):
        self.click(page)
        assert self.check_visibility(link)
