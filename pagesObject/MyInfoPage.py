from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import page

from pagesObject.BasePage import BasePage


class MyInfoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        #locators
        self.url_myInfo = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7"
        self.contact_details = page.get_by_role("link", name="Contact Details")
        self.titre_bloc_contact_details = page.locator("h6.oxd-text", has_text="Contact Details")
        self.champ_home = page.locator("input[modelmodifiers='[object Object]']").nth(0)

        #methodes
    def verifier_url_page_my_info(self):
        expect(self.page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7" , timeout=10000)

    def cliquer_sur_contact_details(self):
        self.cliquer_sur_un_element(self.contact_details)
        self.verifier_le_texte_de_lelement(self.titre_bloc_contact_details, "Contact Details")

    def renseigner_le_champ_home(self):
        self.remplir_un_champ(self.champ_home, "0146309618")
        expect(self.champ_home).to_have_value("0146309618")
