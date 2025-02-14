import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import chromedriver_autoinstaller



@pytest.fixture()
def setup(browser):
    """Fixture to initialize WebDriver based on browser selection"""
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")  # Run Chrome in headless mode
        driver = webdriver.Chrome(options=options)
    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--headless")
        driver = webdriver.Edge(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()  # Ensure the browser is closed after the test


def pytest_addoption(parser):
    """Allows passing browser choice via command line"""
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")


@pytest.fixture()
def browser(request):
    """Retrieves the browser value from CLI options"""
    return request.config.getoption("--browser")


# Customizing HTML Report
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Hook to add extra metadata to the HTML report"""
    config._metadata["Project Name"] = "Open Cart"
    config._metadata["Module Name"] = "Register Module"
    config._metadata["Tester Name"] = "Pavan"


@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    """Hook to remove unnecessary metadata from HTML report"""
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not hasattr(config, 'slaveinput'):
        import allure_pytest
        config.pluginmanager.register(allure_pytest.AllurePlugin())