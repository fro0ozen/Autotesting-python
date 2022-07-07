from selenium.webdriver.common.by import By


class MainPageLocators:
    ENTER_BUTTON_LOCATOR = (By.XPATH, "//div[contains(@class,'responseHead-module-button')]")
    ENTER_EMAIL_LOCATOR = (By.NAME, "email")
    ENTER_PASSWORD_LOCATOR = (By.NAME, "password")
    ENTER_LOCATOR = (By.XPATH, "//div[contains(@class,'authForm-module-button')]")
    ERROR_LABEL_LOCATOR = (By.XPATH, "//div/div[@class='formMsg_title']")


class BaseHomeLocators:
    AUDITORY_LOCATOR = (By.XPATH, "//a[@href='/segments']")


class DashboardLocators(BaseHomeLocators):
    NEW_FIRST_CAMPAIGN_LOCATOR = (By.XPATH, "//a[@href='/campaign/new']")
    NEW_CAMPAIGN_LOCATOR = (By.XPATH, "//div[contains(@class, 'button-module-blue')]/div") #dashboard-module-createButtonWrap \ button-module-textWrapper

    TRAFFIC_LOCATOR = (By.XPATH, "//div[contains(@class, '_traffic')]")
    URL_FIELD_LOCATOR = (By.XPATH, "//input[@data-gtm-id='ad_url_text']")
    BANNER_LOCATOR = (By.ID, "patterns_banner_4")
    UPLOAD_BUTTON_LOCATOR = (By.XPATH, "//div[contains(@class,'roles-module-buttonWrap')]//child::input")
    CAMPAIGN_NAME_FIELD_LOCATOR = (By.XPATH, "//div[contains(@class, 'input_campaign-name')]//child::input")
    CREATE_CAMPAIGN_LOCATOR = (By.XPATH, "//div[contains(@class, 'footer__button')]/button")
    PATTERN_CAMPAIGN_NAME_LOCATOR = (By.XPATH, "//a[@title='{}']")

    PATTERN_SETTINGS_BUTTON_LOCATOR = (
        By.XPATH,
        "//a[@title='{}']//ancestor::div[contains(@class, 'main-module-Cell')]/following-sibling::div"
    )
    DELETE_BUTTON_LOCATOR = (By.XPATH, "//li[@data-id='3']")


class SegmentsLocators(BaseHomeLocators):
    NEW_FIRST_SEGMENT_LOCATOR = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    NEW_SEGMENT_LOCATOR = (By.XPATH, "//div/button[@data-class-name='Submit']")

    CHECKBOX_LOCATOR = (By.XPATH, "//input[contains(@class, 'adding-segments-source__checkbox')]")
    ADD_SEGMENT_BUTTON_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'adding-segments-modal')]/button[@data-class-name='Submit']"
    )
    NAME_FIELD_LOCATOR = (By.XPATH, "//div[contains(@class, 'input_create-segment')]//child::input")
    CREATE_SEGMENT_LOCATOR = (By.XPATH, "//button[contains(@class, 'button_submit')]")
    PATTERN_SEGMENT_NAME_LOCATOR = (By.XPATH, "//a[@title='{}']")
    PATTERN_DELETE_BUTTON_LOCATOR = (
        By.XPATH,
        "//a[@title='{}']//ancestor::div[contains(@class, 'main-module-Cell')]//following-sibling::div[contains(@data-test, 'remove')]"
    )
    REMOVE_CONFIRM_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'button_confirm-remove')]")
