import pytest
from repo.pageObjects.GreenKart import GreenKart
from repo.pageObjects.HomePage import HomePage
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )

@pytest.fixture(scope='session')
def driver(request):
    driver = request.config.getoption("--browser")
    if driver == 'chrome':
        driver = webdriver.Chrome()
    elif driver == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception(f'Browser "{driver}" is not supported')

    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def homePage(driver):
    return HomePage(driver)

@pytest.fixture(scope='session')
def greenKart(driver):
    return GreenKart(driver)

