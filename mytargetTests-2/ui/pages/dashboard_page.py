from ui.pages.base_page import BasePage
from ui.pages.segments_page import SegmentsPage
from ui.locators.basic_locators import DashboardLocators
import allure


# Страница кампаний
class DashboardPage(BasePage):
    url = "https://target.my.com/dashboard"
    locators = DashboardLocators()

    @allure.step("Going to segments")
    def go_to_segments(self, locator):
        self.logger.info(f"Go to segments page")
        self.click(locator)
        return SegmentsPage(self.driver)

    @allure.step("Creating new campaign with name: {name}")
    def create_new_campaign(self, name, file_path):
        self.logger.info(f"Create new campaign {name}")

        url = "mail.ru"
        if self.check_visibility(self.locators.NEW_CAMPAIGN_LOCATOR, timeout=10):
            self.click(self.locators.NEW_CAMPAIGN_LOCATOR, timeout=10)
        elif self.check_visibility(self.locators.NEW_FIRST_CAMPAIGN_LOCATOR, timeout=10):
            self.click(self.locators.NEW_FIRST_CAMPAIGN_LOCATOR, timeout=10)
        self.click(self.locators.TRAFFIC_LOCATOR, timeout=10)
        self.clear_and_send_keys(self.locators.URL_FIELD_LOCATOR, url, timeout=15)
        self.check_visibility(self.locators.CAMPAIGN_NAME_FIELD_LOCATOR)
        self.clear_and_send_keys(self.locators.CAMPAIGN_NAME_FIELD_LOCATOR, name, timeout=10)
        self.click(self.locators.BANNER_LOCATOR)

        input_field = self.find(self.locators.UPLOAD_BUTTON_LOCATOR)
        input_field.send_keys(file_path)
        self.check_visibility(self.locators.CREATE_CAMPAIGN_LOCATOR)
        self.click(self.locators.CREATE_CAMPAIGN_LOCATOR)
        return (
                self.locators.PATTERN_CAMPAIGN_NAME_LOCATOR[0],
                self.locators.PATTERN_CAMPAIGN_NAME_LOCATOR[1].format(name)
                )

    @allure.step("Deleting campaign with name: {name}")
    def delete_campaign(self, name, locator):
        self.logger.info(f"Delete last created campaign")

        settings_button_locator = (
            self.locators.PATTERN_SETTINGS_BUTTON_LOCATOR[0],
            self.locators.PATTERN_SETTINGS_BUTTON_LOCATOR[1].format(name)
        )
        self.click(settings_button_locator)
        self.click(self.locators.DELETE_BUTTON_LOCATOR)
        self.driver.refresh()
        self.check_visibility(locator, visible=False)
