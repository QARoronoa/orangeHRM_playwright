import pytest
from playwright.sync_api import Playwright
from data.refactor_data import refactor_data

@pytest.fixture(scope="function")
def setup(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield page

    context.close()
    browser.close()


@pytest.fixture(scope="function")
def fill_form_addEmployee():
    return refactor_data.add_employee()