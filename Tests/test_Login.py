import pytest
from Tests.test_base import BaseTest
from Pages.LoginPages import LoginPage
from Config.config import TestData

class Test_Login_By_Username(BaseTest):

   def test_login_page_title(self):
      self.loginPage = LoginPage(self.driver)
      title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
      assert title == TestData.LOGIN_PAGE_TITLE

   def test_login_with_invalid_username(self):
      self.loginPage = LoginPage(self.driver)
      self.loginPage.do_login(TestData.INVALID_USERNAME, TestData.INVALID_PASSWORD)
      text = self.loginPage.get_element_text(self.loginPage.LOGIN_ERROR_ALERT)
      assert TestData.LOGIN_ERROR_MESSAGE == text

   def test_login_by_username(self):
      self.loginPage = LoginPage(self.driver)
      self.loginPage.clear_user_input()
      self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
      assert TestData.LOGIN_PAGE_USERINFO == self.loginPage.get_login_status()

class Test_Login_with_ThirdParty(BaseTest):

   def test_login_by_facebook(self):
      self.loginPage = LoginPage(self.driver)
      self.loginPage.do_click(self.loginPage.FACEBOOK_LOGIN_BUTTON)
      title = self.loginPage.get_title(TestData.FACEBOOK_LOGIN_PAGE_TITLE)
      assert TestData.FACEBOOK_LOGIN_PAGE_TITLE == title

   def test_login_by_apple(self):
      self.loginPage = LoginPage(self.driver)
      self.loginPage.do_click(self.loginPage.APPLE_LOGIN_BUTTON)
      title = self.loginPage.get_title(TestData.APPLE_LOGIN_PAGE_TITLE)
      assert TestData.APPLE_LOGIN_PAGE_TITLE == title

   def test_login_by_google(self):
      self.loginPage = LoginPage(self.driver)
      self.loginPage.do_click(self.loginPage.GOOGLE_LOGIN_BUTTON)
      title = self.loginPage.get_title(TestData.GOOGLE_LOGIN_PAGE_TITLE)
      assert TestData.GOOGLE_LOGIN_PAGE_TITLE == title