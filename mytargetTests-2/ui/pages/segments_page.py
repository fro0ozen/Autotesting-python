from ui.pages.base_page import BasePage
from ui.locators.basic_locators import SegmentsLocators
import allure


# Страница аудиторий
class SegmentsPage(BasePage):
    url = "https://target.my.com/segments/segments_list"
    locators = SegmentsLocators()

    @allure.step("Creating new segment with name: {name}")
    def create_new_segment(self, name):
        self.logger.info(f"Create new segment {name}")

        if self.check_visibility(self.locators.NEW_FIRST_SEGMENT_LOCATOR, timeout=10):
            self.click(self.locators.NEW_FIRST_SEGMENT_LOCATOR, timeout=5)
        elif self.check_visibility(self.locators.NEW_SEGMENT_LOCATOR, timeout=10):
            self.click(self.locators.NEW_SEGMENT_LOCATOR, timeout=5)

        self.click(self.locators.CHECKBOX_LOCATOR)
        self.click(self.locators.ADD_SEGMENT_BUTTON_LOCATOR)

        self.clear_and_send_keys(self.locators.NAME_FIELD_LOCATOR, name)
        self.click(self.locators.CREATE_SEGMENT_LOCATOR)
        return (
                self.locators.PATTERN_SEGMENT_NAME_LOCATOR[0],
                self.locators.PATTERN_SEGMENT_NAME_LOCATOR[1].format(name)
                )

    @allure.step("Deleting segment with name: {name}")
    def delete_just_created_segment(self, name, locator):
        self.logger.info(f"Delete just created segment")

        delete_button_locator = (
            self.locators.PATTERN_DELETE_BUTTON_LOCATOR[0],
            self.locators.PATTERN_DELETE_BUTTON_LOCATOR[1].format(name)
        )
        self.click(delete_button_locator)
        self.click(self.locators.REMOVE_CONFIRM_BUTTON_LOCATOR)
        self.check_visibility(locator, visible=False)
