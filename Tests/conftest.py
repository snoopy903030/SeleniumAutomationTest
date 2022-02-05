import pytest
from selenium import webdriver
from Config.config import TestData

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        wd = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
    #
    # if request.params == "firefox":
    #     wd = webdriver.Chrome(TestData.FIREFOX_EXECUTABLE_PATH)

    request.cls.driver = wd
    yield
    wd.close()
