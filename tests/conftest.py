import os
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from wb_ui_test_project.utils import attach

DEFAULT_BROWSER_VERSION = '126.0'


def pytest_addoption(parser):
    parser.addoption(
        "--browser_version",
        default="126.0",
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def browser_config(request):
    browser_version = request.config.getoption("--browser_version")
    browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    selenoid = os.getenv('SELENOID_URL')
    driver = webdriver.Remote(command_executor=f"https://{login}:{password}@{selenoid}/wd/hub",
                              options=options)
    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://www.wildberries.ru/"
    browser.config.timeout = 20
    yield

    attach.screenshot(browser)
    attach.html(browser)
    attach.video(browser)

    browser.quit()
