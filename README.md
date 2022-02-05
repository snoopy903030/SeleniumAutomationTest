# SeleniumAutomationTest
This Project is coding by python selenium to automated Spotify UI testing https://open.spotify.com/

Testcases includes
1.User Login 
2.User sign up


Before execute the project, check Config.py to make sure your configurations are set correctly 
# UPDATE Config\congif.py
webdriver_path = "C:\Users\CathyLiu\chromedriver.exe" 

# INSTALL PYTEST 
pip install pytest 
pip install pytest-html


# RUN TESTCASES FROM YOUR TERMINAL
# Run Specific Test Cases,  -sv is to log the print message
pytest Tests/test_Login.py::Test_Login_By_Username::test_login_page_title -sv

# Run All Test Cases in file
pytest Tests/test_Login.py



