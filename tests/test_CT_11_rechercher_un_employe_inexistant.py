import time

import allure

from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.PimPage import PimPage

def test_rechercher_un_employer_existant(setup, fill_form_addEmployee):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    pim_page = PimPage(setup)

    with allure.step("se connecter"):
        login_page.verifier_titre_de_la_page('OrangeHRM')
        login_page.remplir_les_credentials_avec_credentials_valides()
        login_page.cliquer_sur_le_bouton_login()

    with allure.step("Redirection vers page d'accueil"):
        home_page.verifier_la_redirection_vers_dashboard()

    with allure.step("naviguer vers PIM page"):
        pim_page.cliquer_sur_menu_pim()
        pim_page.verifier_redirection_vers_PIM_page()

    with allure.step("entrer le nom dun employe"):
        pim_page.entrer_le_nom_dun_employeur("kjkjkj")
        pim_page.cliquer_sur_le_bouton_search()

    with allure.step("Confirmation de la recherche nul"):
        pim_page.verifier_la_recherche_employer("No Records Found")




