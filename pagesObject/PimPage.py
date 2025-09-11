from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import page

from pagesObject.BasePage import BasePage


class PimPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        #locators
        self.bouton_pim = page.locator("span.oxd-text", has_text="PIM")
        self.titre_pim_page = page.locator("h6.oxd-text--h6", has_text="PIM")
        self.add_employee_page_lien = page.get_by_role("link", name="Add Employee")
        self.add_employee_page_titre = page.locator(".orangehrm-main-title")
        self.champ_firtName = page.get_by_placeholder("First Name")
        self.champ_lastName = page.get_by_placeholder("Last Name")
        self.bouton_ajout_photo = page.locator(".employee-image-wrapper")
        self.bouton_save = page.get_by_role("button", name="Save")
        self.erreur_champ_prenom = page.locator("span.oxd-input-field-error-message", has_text="Required")
        self.employe_name = page.get_by_placeholder("Type for hints...").nth(0)
        self.bouton_search = page.get_by_role("button", name="Search")
        self.recherche_OK= page.locator('span.oxd-text', has_text="(1) Record Found")
        self.recherche_NOK = page.locator('span.oxd-text', has_text="No Records Found")

        #methodes
    def cliquer_sur_menu_pim(self):
        self.cliquer_sur_un_element(self.bouton_pim)
        # self.page.wait_for_timeout(1000)

    def verifier_redirection_vers_PIM_page(self):
        self.verifier_element_visible(self.titre_pim_page)

    def cliquer_sur_bouton_add_employee(self):
        self.cliquer_sur_un_element(self.add_employee_page_lien)
        self.verifier_le_texte_de_lelement(self.add_employee_page_titre, "Add Employee")

    def remplir_formulaire_add_employee(self, firstName, lastName):
        self.remplir_un_champ(self.champ_firtName, firstName)
        self.remplir_un_champ(self.champ_lastName, lastName)

    def ajouter_une_photo(self):
        self.page.locator("input.oxd-file-input").set_input_files(r"C:\Users\Administrateur\Pictures\Capture.PNG")

    def cliquer_sur_save(self):
        self.cliquer_sur_un_element(self.bouton_save)

    def verifier_message_erreur_champ_prenom(self):
        self.verifier_le_texte_de_lelement(self.erreur_champ_prenom, "Required")

    def entrer_le_nom_dun_employeur(self,text):
        self.remplir_un_champ(self.employe_name, text)

    def cliquer_sur_le_bouton_search(self):
        self.cliquer_sur_un_element(self.bouton_search)
        # self.verifier_le_texte_de_lelement(self.recherche_OK, "(1) Record Found")

    def verifier_la_recherche_employer(self, text):
        self.verifier_le_texte_de_lelement(self.recherche_NOK, text)