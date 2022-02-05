from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    USERNAME = (By.ID, "login-username")
    PASSWORD = (By.ID, "login-password")
    LOGIN_BUTTON = (By.ID, "login-button")
    USER_INFO = (By.CSS_SELECTOR, '[data-testid="user-info"]')
    FACEBOOK_LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-testid="facebook-login"]')
    APPLE_LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-testid="apple-login"]')
    GOOGLE_LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-testid="google-login"]')
    LOGIN_ERROR_ALERT = (By.XPATH, '//p[@class="Type__TypeElement-goli3j-0 craHza sc-fotOHu gGrrEB"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    def get_login_status(self):
        status_text = self.get_element_text(self.USER_INFO)
        return status_text

    #This is to clear all the text in username and password feild
    def clear_user_input(self):
        self.do_click(self.USERNAME)
        a = ActionChains(self.driver)
        a.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
        a.send_keys(Keys.BACKSPACE).perform()

        self.do_click(self.PASSWORD)
        b = ActionChains(self.driver)
        b.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
        b.send_keys(Keys.BACKSPACE).perform()
