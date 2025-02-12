#import Service
import pytest
from selenium import webdriver


@pytest.fixture()
def setup(self, browser):
    if browser == "chrome":
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service("C:\browsers drivers\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(service=self.serv_obj)
    elif browser == "edge":
        from selenium.webdriver.edge.service import Service
        serv_obj = Service("C:\browsers drivers\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=self.serv_obj)
    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        serv_obj = Service("C:\browsers drivers\geckodriver-v0.34.0-win64\geckodriver.exe")
        driver = webdriver.Firefox(service=self.serv_obj)
    return driver


def pytest_addoption(parser):  # This will get the value from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# customizing reHTML Report
# It is hook for Adding Environment info to HTML Report
#def pytest_configure(config):
#config._metadata['Project Name'] = 'open cart'
#config._metadata['Module Name'] = 'Register Module'
#config._metadata['Tester Name'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
#@pytest.mark.optionalhook
#def pytest_metadata(metadata):
#metadata.pop("JAVA_HOME", None)
#metadata.pop("Plugins", None)
