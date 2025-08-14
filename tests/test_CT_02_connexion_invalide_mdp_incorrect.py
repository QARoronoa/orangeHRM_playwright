from pagesObject.LoginPage import LoginPage

def test_connexion_invalide_mdp_incorrect(setup):
    login_page = LoginPage(setup)

    #se connecter
    login_page.verifier_titre_de_la_page('OrangeHRM')
    login_page.remplir_les_credentials_avec_credentials_invalides()
    login_page.cliquer_sur_le_bouton_login()
    login_page.verifier_le_message_erreur_connexion_invalide()



