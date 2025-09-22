import time

import allure

from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.MyInfoPage import MyInfoPage

def test_modifier_la_fiche_dun_profil(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    myInfo_page = MyInfoPage(setup)


    with allure.step("se connecter"):
        login_page.verifier_titre_de_la_page('OrangeHRM')
        login_page.remplir_les_credentials_avec_credentials_valides()
        login_page.cliquer_sur_le_bouton_login()

    with allure.step("Redirection vers page d'accueil"):
        home_page.verifier_la_redirection_vers_dashboard()

    with allure.step("naviguer vers My info page"):
        home_page.cliquer_sur_my_info()

    with allure.step("naviguer vers contact details"):
        myInfo_page.cliquer_sur_contact_details()

    with allure.step("remplir le champ home"):
        myInfo_page.renseigner_le_champ_home()




