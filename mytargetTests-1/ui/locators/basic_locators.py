from selenium.webdriver.common.by import By

COMPANY_ACTIVATED_LOCATOR = (By.XPATH, "//a[contains(@class, 'center-module-activeButton') and @href='/dashboard']")

ENTER_BUTTON_LOCATOR = (By.XPATH, "//div[contains(@class,'responseHead-module-button')]")
TITLE_LOCATOR = (By.XPATH, "//a[contains(@class, 'responseHead-module-logoLink')]")

ENTER_EMAIL_LOCATOR = (By.NAME, "email")
ENTER_PASSWORD_LOCATOR = (By.XPATH, "//input[@type = 'password']")
ENTER_LOCATOR = (By.XPATH, "//div[contains(@class,'authForm-module-button')]")

EXIT_MENU_LOCATOR = (By.XPATH, "//a[@href='/logout']/ancestor::ul/preceding-sibling::div")
EXIT_BUTTON_LOCATOR = (By.XPATH, "//a[@href='/logout']")

PROFILE_LOCATOR = (By.XPATH, "//a[@href='/profile']")
PROFILE_NAME_LOCATOR = (By.XPATH, "//div[@data-name='fio']/div[@class='input__wrap']/input")
PROFILE_NUMBER_LOCATOR = (By.XPATH, "//div[@data-name='phone']/div[@class='input__wrap']/input")
PROFILE_SAVE_BUTTON_LOCATOR = (By.XPATH, "//a[@href='false']/parent::div/following-sibling::div/button/div")
SUCCESS_SAVE_LOCATOR = (By.XPATH, "//div[@data-class-name='SuccessView']/div[contains(@class, '_notification__content')]")

PAGE_COMPANY_LOCATOR = (By.XPATH, "//a[@href='/dashboard']")
PAGE_AUDIENCE_LOCATOR = (By.XPATH, "//a[@href='/segments']")
PAGE_BALANCE_LOCATOR = (By.XPATH, "//a[@href='/billing']")
PAGE_STATISTIC_LOCATOR = (By.XPATH, "//a[@href='/statistics']")
PAGE_TOOLS_LOCATOR = (By.XPATH, "//a[@href='/tools']")

PAGE_AUDIENCE_ACTIVATED_LOCATOR = (By.XPATH, "//a[contains(@class, 'center-module-activeButton') and @href='/segments']")
PAGE_BALANCE_ACTIVATED_LOCATOR = (By.XPATH, "//a[contains(@class, 'center-module-activeButton') and @href='/billing']")
PAGE_STATISTIC_ACTIVATED_LOCATOR = (By.XPATH, "//a[contains(@class, 'center-module-activeButton') and @href='/statistics']")
PAGE_TOOLS_ACTIVATED_LOCATOR = (By.XPATH, "//a[contains(@class, 'center-module-activeButton') and @href='/tools']")
