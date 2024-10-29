import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def base_url():
    """Fixture to provide the base URL of the Sauce Labs website."""
    return "https://www.saucedemo.com/"


@pytest.fixture(scope="session")
def driver(base_url):
    """Fixture to provide a WebDriver instance."""
    driver = webdriver.Chrome()
    driver.get(base_url)
    yield driver
    driver.quit()
