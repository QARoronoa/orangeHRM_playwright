import time

from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage


def test_verification_menu_principal(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)

    # se connecter
    login_page.verifier_titre_de_la_page('OrangeHRM')
    login_page.remplir_les_credentials_avec_credentials_valides()
    login_page.cliquer_sur_le_bouton_login()
    home_page.verifier_la_redirection_vers_dashboard()

    #verification menu test
    home_page.verifier_menus_volet_gauche()
