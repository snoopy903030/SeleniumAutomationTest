from selenium import webdriver

# Globle variable
global driver
driver = webdriver.Chrome('C:\\Webdriver\\chromedriver.exe')
global url_spotify
url_spotify = "https://accounts.spotify.com/en/login"
print("----Global-------")
global main_windowhandle

def OpenURL():
    print("In OpenURL")
    print(url_spotify)
    driver.get(url_spotify)

    print("driver is none below")
    print(driver is None)

    main_windowhandle = driver.window_handles[0]
    print("main window handle is below")
    print(main_windowhandle[0])


    driver.implicitly_wait(5)
    driver.maximize_window()
    print(driver.title)

# this function is using for checking if web driver can find the objective element,
# strMethod stands for the method when find_elements, can be "id","css_selector","xpath"
# strEleIdentify stands for the key values of the sepecify finding method
def FindElement(strMethod, strEleIdentify):
    if strMethod == "id":
        Element = driver.find_elements_by_id(strEleIdentify)
    if strMethod == "css_selector":
        Element = driver.find_elements_by_css_selector(strEleIdentify)
    elif strMethod == "xpath":
        Element = driver.find_element_by_xpath(strEleIdentify)

    if (len(Element)>0 and len(Element) == 1):
        print('Find the unique object web driver element successful.')
        return Element[0]
    else:
        print("The object element doesn't exist.")
        return None


def CheckWindowTitel(strExpectedTitle):
    strActual = driver.title
    strExpected = strExpectedTitle
    if (strActual.find(strExpected)!=-1):
        print("The Title of current window is: "+strActual + ", Pass the test!")
        return True
    else:
        print("The Title of current window is: " + strActual + ", Test Failed!")
        return False