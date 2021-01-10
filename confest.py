import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
