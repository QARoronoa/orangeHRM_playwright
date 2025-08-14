import allure
from locator import locator
from playwright.sync_api import Page, expect, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page


    #methodes
    @allure.step("Le titre de la page est '{title}'")
    def verifier_titre_de_la_page(self, title):
        expect(self.page).to_have_title(title)

    @allure.step('L element est visible')
    def verifier_element_visible(self, locator: Locator):
        expect(locator).to_be_visible()

    @allure.step('clique sur l element OK')
    def cliquer_sur_un_element(self, locator: Locator):
        expect(locator).to_be_visible()
        expect(locator).to_be_enabled()
        locator.click()

    @allure.step('Le texte "{texte}" est visible')
    def verifier_le_texte_de_lelement(self, locator: Locator ,texte):
        expect(locator).to_be_visible()
        expect(locator).to_have_text(texte)

    @allure.step("Remplir le champ avec : '{text}'")
    def remplir_un_champ(self, locator: Locator, text):
        expect(locator).to_be_visible()
        locator.clear()
        locator.fill(text)
