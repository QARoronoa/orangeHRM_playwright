import time

from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.MyInfoPage import MyInfoPage

def test_naviguer_vers_myInfo(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    myInfo_page = MyInfoPage(setup)

    # se connecter
    login_page.verifier_titre_de_la_page('OrangeHRM')
    login_page.remplir_les_credentials_avec_credentials_valides()
    login_page.cliquer_sur_le_bouton_login()
    home_page.verifier_la_redirection_vers_dashboard()

    #naviguer vers my info
    home_page.cliquer_sur_my_info()
    myInfo_page.verifier_url_page_my_info()
