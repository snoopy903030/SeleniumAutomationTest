from selenium.webdriver.common.action_chains import ActionChains
from Commons import *

# Check if button login wigh Facebook\Apple\Google are exist and if needs to be click
def loginwithOtherAccount(AccountType,btn_Click):

    print("Enter Login with other aacount")
    css_value = '[analytics-event="'+ AccountType + " Button\"]"
    btn_LoginwithAccount = FindElement("css_selector",css_value )

    if (btn_LoginwithAccount != None):
        print("The button [Continue with "+ AccountType +"] exist.")
        if btn_Click != 0:
            btn_LoginwithAccount.click()
    else:
        print("The button [Continue with "+ AccountType +"] doesn't exist!'")

# Check if Username text box exist and type User as required
def InputUsername(strUsername):

    tbox_Username = FindElement("id", "login-username")
    if (tbox_Username != None):
        print('The username text box is exist.Type the username as: '+strUsername)
    else:
        print('Cannot find the username text box!')

    if (strUsername != ""):
        tbox_Username.send_keys(strUsername)

# Check if Password text box exist and Type password as required
def InputPassword(strPassword):

    tbox_Pwd = FindElement("id","login-password")
    if (tbox_Pwd != None):
        print('The passowrd text box is exist.Type the password as: '+strPassword)
    else:
        print('Cannot find the password text box!')

    if (strPassword != ""):
        tbox_Pwd.send_keys(strPassword)

#Click Login Button, when boolClick = True, click the button
def ClickbtnLogin(boolClick):

    btn_login = FindElement("css_selector","#login-button")
    if (btn_login != None):
        print('The Login button is exist.')
    else:
        print("The login button doesn't exist.")

    if (boolClick):
        # move mouse to objective area
        action = ActionChains(driver)
        action.move_to_element(btn_login)
        action.click(btn_login).perform()

#Check Remember me checkbox as required, if boolCheck == True, states this check box needs to be checked
def ClickRememberMe(boolCheck):

    chkbox_RememberMe = FindElement("css_selector",'input[id="login-remember"]')
    if (chkbox_RememberMe != None):
        print('Remember me check box is exist.')

    if (boolCheck == False):
        print("Remember Me status is: "+ str(chkbox_RememberMe.is_selected()))
        # create action chain object
        action = ActionChains(driver)
        #perform movement
        action.move_to_element(chkbox_RememberMe).click().perform()
        print("Remember Me status of selected: " + str(chkbox_RememberMe.is_selected()))


# Check if the error messages shown as expected
def ErrorAlert(strExpUsername_Error, strExpPwdError, strExpGeneralError):

    msg_Alert = FindElement("css_selector", ".alert span")
    error_Username = FindElement("css_selector","[ng-if*=\"username.$error.required\"]")
    error_Pwd      = FindElement("css_selector","[ng-if*=\"password.$error.required\"]")

    if (error_Username != None):
        strError_username = error_Username.text
        print("Username Error: "+ strError_username)
    else:
        print("There's no error when puting username.")
        strError_username = None

    if (error_Pwd != None):
        strError_pwd = error_Pwd.text
        print("Password Error: "+strError_pwd)
    else:
        print("There's no Error when putting password.")
        strError_pwd = None

    if (msg_Alert != None):
        strAlertError = msg_Alert.text
        print("Login Error: "+ strAlertError)
    else:
        print("There's no Alert Error.")
        strAlertError = None

    if (strExpUsername_Error != strError_username):
        print("Expected Username Error: "+strExpUsername_Error)
    if (strError_pwd !=strExpPwdError):
        print("Expected Password Error: "+strExpPwdError)
    if (strExpGeneralError != strAlertError):
        print("Expected general Alert : "+strExpGeneralError)
        return False

    if (strError_username == strExpUsername_Error and strError_pwd == strExpPwdError and strAlertError == strExpGeneralError):
        return True