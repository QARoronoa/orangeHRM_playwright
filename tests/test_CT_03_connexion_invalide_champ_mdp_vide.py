import time

from pagesObject.LoginPage import LoginPage

def test_connexion_invalide_champ_mdp_vide(setup):
    login_page = LoginPage(setup)

    #se connecter
    login_page.verifier_titre_de_la_page('OrangeHRM')
    login_page.remplir_les_credentials_avec_champ_mdp_vide()
    login_page.cliquer_sur_le_bouton_login()
    login_page.verifier_message_alerte_champ_vide()




