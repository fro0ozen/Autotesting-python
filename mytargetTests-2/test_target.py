from base import BaseCase
import pytest
import allure


@allure.feature("UI tests")
@allure.story("Tests by section")
class TestTarget(BaseCase):

    @allure.testcase("Creating campaign")
    @allure.description("""Creating a new advertising campaign
            """)
    @pytest.mark.UI
    def test_add_campaign(self, dashboard_fixture, file_path):
        name, dashboard_page = dashboard_fixture
        locator = dashboard_page.create_new_campaign(name, file_path)
        with allure.step(f"Has a company been created with name: {name}"):
            assert dashboard_page.check_visibility(locator, timeout=10)
        dashboard_page.delete_campaign(name, locator)

    @allure.testcase("Creating auditory")
    @allure.description("""Creating a new audience segment
                """)
    @pytest.mark.UI
    def test_new_auditory(self, new_segment):
        name, locator, segment_page = new_segment
        with allure.step(f"Has a segment been created with name: {name}"):
            assert segment_page.check_visibility(locator)
        segment_page.delete_just_created_segment(name, locator)

    @allure.testcase("Deleting auditory")
    @allure.description("""Deleting an audience segment
                    """)
    @pytest.mark.UI
    def test_delete_auditory(self, new_segment):
        name, locator, segment_page = new_segment
        segment_page.delete_just_created_segment(name, locator)
        with allure.step(f"Has a segment been deleted with name: {name}"):
            assert segment_page.check_visibility(locator, visible=False)


@allure.feature("UI tests")
@allure.story("Negative login tests")
class TestNegativeTarget(BaseCase):

    @allure.testcase("Login with wrong password")
    @allure.description("""An attempt to log in with an invalid password
    """)
    @pytest.mark.UI
    def test_login_wrong_password(self):
        self.main_page.login(password='12345678')
        with allure.step("Is the login not successful"):
            assert self.main_page.check_visibility(self.main_page.locators.ERROR_LABEL_LOCATOR)

    @allure.testcase("Login with wrong email")
    @allure.description("""An attempt to log in with an invalid email
        """)
    @pytest.mark.UI
    def test_login_wrong_email(self):
        self.main_page.login(email="abc123@mail.ru")
        with allure.step("Is the login not successful"):
            assert self.main_page.check_visibility(self.main_page.locators.ERROR_LABEL_LOCATOR)
