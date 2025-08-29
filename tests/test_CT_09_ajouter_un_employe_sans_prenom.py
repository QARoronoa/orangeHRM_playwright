import time

from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.PimPage import PimPage

def test_ajouter_un_employe_sans_prenom(setup, fill_form_addEmployee):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    pim_page = PimPage(setup)

    # se connecter
    login_page.verifier_titre_de_la_page('OrangeHRM')
    login_page.remplir_les_credentials_avec_credentials_valides()
    login_page.cliquer_sur_le_bouton_login()
    home_page.verifier_la_redirection_vers_dashboard()

    #naviguer vers PIM page
    pim_page.cliquer_sur_menu_pim()
    pim_page.verifier_redirection_vers_PIM_page()

    #cliquer sur add employee
    pim_page.cliquer_sur_bouton_add_employee()

    #remplir formulaire
    pim_page.remplir_formulaire_add_employee(fill_form_addEmployee["firstName2"],
                                             fill_form_addEmployee["lastName"])
    pim_page.ajouter_une_photo()
    pim_page.cliquer_sur_save()
    pim_page.verifier_message_erreur_champ_prenom()

