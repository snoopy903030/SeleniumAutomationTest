import pytest
import pytest_html
from selenium import webdriver
import sys
from Login import *

class Test_LoginwithThirdParty:

    def setup_method(self):
        print("----set up-------")
        OpenURL()

    def teardown_class(self):
        driver.quit()
        print("----tear down class---")

    def test_LoginwithFacebook(self):
        print("Login with Facebook")
        loginwithOtherAccount("Facebook", 1)
        assert CheckWindowTitel("Facebook")

    def test_LoginwithApple(self):
        print("Login with Apple")
        loginwithOtherAccount("Apple", 1)
        assert CheckWindowTitel("Apple")

    def test_LoginwithGoogle(self):
        print("Login with Google")
        loginwithOtherAccount("Google", 1)
        assert CheckWindowTitel("Google")

class Test_ValidLoginInfo:
    def setup_method(self):
        print("-----Initialize Test Valid Login TestCases------")
        OpenURL()

    def teardown_method(self):
        print('teardown')

    def test_LoginSuccessful(self):
        InputUsername('21hqg5lqvirkobltn7hbnmmii')
        InputPassword('Test!23456')
        ClickRememberMe(False)
        ClickbtnLogin(True)
        ErrorAlert()