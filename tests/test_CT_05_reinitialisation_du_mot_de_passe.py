import time

from pagesObject.LoginPage import LoginPage


def test_reinitialisation_du_mdp(setup):
    login_page = LoginPage(setup)

    login_page.cliquer_sur_le_lien_mdp_oublie()
    login_page.verifier_la_redirection_vers_la_page_reset_pwd()
    login_page.remplir_le_champ_username()
    login_page.cliquer_sur_le_bouton_reset_password()
    login_page.verifier_l_envoi_du_lien_reinitialisation()

    time.sleep(3)
