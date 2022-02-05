import pytest
import pytest_html
from Login import *

class Test_ValidLoginInfo:

    def setup_method(self):
        print("-----Initialize Test Valid Login TestCases------")
        OpenURL()

    def teardown_method(self):
        btn_Logout = driver.find_element_by_css_selector('button[ng-click="logout()"]')
        btn_Logout.click()
        print('----Log out finished----')
        print(driver.current_url)

    def test_LoginSuccessful(self):

        InputUsername('21hqg5lqvirkobltn7hbnmmii')
        InputPassword('Test!23456')
        ClickRememberMe(False)
        ClickbtnLogin(True)
        if (ErrorAlert(None,None,None)):
            print("No error alert")
        assert CheckWindowTitel("Status")

    def test_LoginSuccessful_RememberMe(self):

        InputUsername('21hqg5lqvirkobltn7hbnmmii')
        InputPassword('Test!23456')
        ClickRememberMe(True)
        ClickbtnLogin(True)
        if (ErrorAlert(None,None,None)):
            print("No error alert")
        assert CheckWindowTitel("Status")

class Test_InvailidLogin:

    def setup_method(self):
        print("-----Initialize Test invalid Login TestCases------")
        OpenURL()

    def teardown_method(self):
        print("quit")

    def test_InvalidUsername(self):
        InputUsername('')
        InputPassword("")
        ClickbtnLogin(True)
        assert ErrorAlert("Please enter your Spotify username or email address.","Please enter your password.",None)

