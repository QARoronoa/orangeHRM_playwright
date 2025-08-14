from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import page

from pagesObject.BasePage import BasePage


class MyInfoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        #locators
        self.url_myInfo = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7"
        #methodes
    def verifier_url_page_my_info(self):
        expect(self.page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7" , timeout=10000)