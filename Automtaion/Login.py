from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Globle variable
global driver
driver = webdriver.Chrome('C:\\Webdriver\\chromedriver.exe')
global url_spotify
url_spotify = "https://accounts.spotify.com/en/login"

strUsername = ""
strPassword = ""


print("----Global-------")

def OpenURL():
    print("In OpenURL")
    driver.get(url_spotify)
    print("driver is none below")
    print(driver is None)

    main_windowhandle = driver.window_handles
    print("main window is none below")
    print(main_windowhandle is None)

    driver.implicitly_wait(5)
    driver.maximize_window()
    print(driver.title)

# Check if button login wigh Facebook\Apple\Google are exist and if needs to be click
def loginwithOtherAccount(AccountType,btn_Click):
    print("Enter Login with other aacount")
    btn_LoginwithAccount = driver.find_elements_by_css_selector('[analytics-event="'+ AccountType + " Button\"]")
    if len(btn_LoginwithAccount) > 0:
        print("The button [Continue with "+ AccountType +"] exist.")
        if btn_Click != 0:
            btn_LoginwithAccount[0].click()
    else:
        print("The button [Continue with "+ AccountType +"] doesn't exist!'")

def CheckWindowTitel(strExpectedTitle):
    strActual = driver.title
    strExpected = strExpectedTitle
    if (strActual.find(strExpected)!=-1):
        print("The Title of current window is: "+strActual + ", Pass the test!")
        return True
    else:
        print("The Title of current window is: " + strActual + ", Test Failed!")
        return False


def InputUsername(strUsername):
    Textbox_Username = driver.find_elements_by_id("login-username")
    if (len(Textbox_Username) > 0):
        print('The username text box is exist.Type the username as: '+strUsername)
    else:
        print('Cannot find the username text box!')
    if (strUsername != ""):
        Textbox_Username[0].send_keys(strUsername)


def InputPassword(strPassword):
    Textbox_pwd = driver.find_elements_by_id("login-password")
    if (len(Textbox_pwd) > 0):
        print('The passowrd text box is exist.Type the password as: '+strPassword)
    else:
        print('Cannot find the password text box!')
    if (strPassword != ""):
        Textbox_pwd[0].send_keys(strPassword)

def ClickbtnLogin(boolClick):
    btn_login = driver.find_elements_by_css_selector("#login-button")
    if (len(btn_login) > 0):
        print('The Login button is exist.')
    else:
        print("The login button doesn't exist.")
    if (boolClick):
        action = ActionChains(driver)
        action.move_to_element(btn_login[0]).click().perform()
        btn_login[0].click()

def ClickRememberMe(boolCheck):
    chkBox_RememberMe = driver.find_elements_by_css_selector('input[id="login-remember"]')
    if (len(chkBox_RememberMe) > 0):
        print('Remember me check box is exist.')
    if (boolCheck == False):
        print("Remember Me status is: "+ str(chkBox_RememberMe[0].is_selected()))

        # create action chain object
        action = ActionChains(driver)
        #perform movement
        action.move_to_element(chkBox_RememberMe[0]).click().perform()
        print("Remember Me status of selected: " + str(chkBox_RememberMe[0].is_selected()))

def ErrorAlert():
    msg_Alert = driver.find_element_by_css_selector(".alert span")
    print(msg_Alert.text)

