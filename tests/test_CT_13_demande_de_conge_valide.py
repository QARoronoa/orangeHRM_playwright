import time

import allure

from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.LeavePage import LeavePage

def test_demande_de_conger(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    leave_page = LeavePage(setup)


    with allure.step("se connecter"):
        login_page.verifier_titre_de_la_page('OrangeHRM')
        login_page.remplir_les_credentials_avec_credentials_valides()
        login_page.cliquer_sur_le_bouton_login()
        home_page.verifier_la_redirection_vers_dashboard()

    with allure.step("se diriger dans le menu leave"):
        home_page.cliquer_sur_Leave()
        leave_page.verifier_redirection_vers_LEAVE_page()

    with allure.step("cliquer sur apply-menu"):
        leave_page.cliquer_sur_apply()


        time.sleep(4)

