import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        s = Service("C://Users//Dell//PycharmProjects//temp_button//drivers//chromedriver.exe")
        driver = webdriver.Chrome(service=s)
    elif browser_name == "firefox":
        s = Service("C://Users//Dell//PycharmProjects//temp_button//drivers//geckodriver.exe")
        driver = webdriver.Firefox(service=s)
    driver.get("https://github.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


