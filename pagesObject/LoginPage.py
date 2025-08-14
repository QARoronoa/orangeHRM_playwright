from pagesObject.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)


    #locators
        self.champ_username = page.get_by_placeholder("Username")
        self.champ_password = page.get_by_placeholder("Password")
        self.bouton_login = page.locator(".oxd-button")
        self.message_erreur_connexion = page.locator("p.oxd-text", has_text="Invalid credentials")
        self.message_alerte_required = page.locator("span.oxd-text", has_text="Required")
        self.bouton_mdp_oublie = page.locator('p.oxd-text', has_text="Forgot your password?")
        self.forgot_pwd_title = page.locator(".orangehrm-forgot-password-title")
        self.bouton_reset_pwd = page.get_by_role("button", name="Reset Password")
        self.message_lien_envoye_avec_success = page.locator(".orangehrm-forgot-password-title")


    #methodes

    def remplir_les_credentials_avec_credentials_valides(self):
        self.remplir_un_champ(self.champ_username, "Admin")
        self.remplir_un_champ(self.champ_password, "admin123")

    def remplir_les_credentials_avec_credentials_invalides(self):
        self.remplir_un_champ(self.champ_username, "Admin")
        self.remplir_un_champ(self.champ_password, "admin12356")

    def remplir_les_credentials_avec_champ_mdp_vide(self):
        self.remplir_un_champ(self.champ_username, "Admin")

    def cliquer_sur_le_bouton_login(self):
        self.cliquer_sur_un_element(self.bouton_login)
        self.page.wait_for_timeout(2000)

    def verifier_le_message_erreur_connexion_invalide(self):
        self.verifier_le_texte_de_lelement(self.message_erreur_connexion, "Invalid credentials")

    def verifier_message_alerte_champ_vide(self):
        self.verifier_le_texte_de_lelement(self.message_alerte_required, "Required")

    def cliquer_sur_le_lien_mdp_oublie(self):
        self.cliquer_sur_un_element(self.bouton_mdp_oublie)

    def verifier_la_redirection_vers_la_page_reset_pwd(self):
        self.verifier_le_texte_de_lelement(self.forgot_pwd_title, "Reset Password")

    def remplir_le_champ_username(self):
        self.champ_username.fill("Admin")

    def cliquer_sur_le_bouton_reset_password(self):
        self.cliquer_sur_un_element(self.bouton_reset_pwd)

    def verifier_l_envoi_du_lien_reinitialisation(self):
        self.verifier_le_texte_de_lelement(self.message_lien_envoye_avec_success, "Reset Password link sent successfully")
