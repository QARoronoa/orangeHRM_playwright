from playwright.sync_api import expect

from pagesObject.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        #locators
        self.texte_dashboard = page.locator('h6.oxd-text', has_text="Dashboard")
        self.menu_user = page.locator(".oxd-userdropdown-name")
        self.bouton_logout = page.locator("a.oxd-userdropdown-link", has_text="Logout")
        self.volet_gauche_menus = page.locator(".oxd-main-menu-item-wrapper")
        self.menu_my_info = page.locator('span.oxd-text', has_text="My Info")


        #methodes
    def verifier_la_redirection_vers_dashboard(self):
        self.verifier_le_texte_de_lelement(self.texte_dashboard,"Dashboard")

    def cliquer_sur_menu_utilisateur(self):
        self.cliquer_sur_un_element(self.menu_user)

    def cliquer_sur_logout(self):
        self.cliquer_sur_un_element(self.bouton_logout)

    def verifier_menus_volet_gauche(self):
        menus_liste = self.page.locator(".oxd-main-menu-item-wrapper").all_inner_texts()
        expect(self.volet_gauche_menus).to_have_text([
            "Admin",
            "PIM",
            "Leave",
            "Time",
            "Recruitment",
            "My Info",
            "Performance",
            "Dashboard",
            "Directory",
            "Maintenance",
            "Claim",
            "Buzz"
        ])
        print(menus_liste)

    def cliquer_sur_my_info(self):
        self.cliquer_sur_un_element(self.menu_my_info)
        self.page.wait_for_timeout(2000)
