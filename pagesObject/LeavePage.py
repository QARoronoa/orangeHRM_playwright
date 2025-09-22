from pagesObject.BasePage import BasePage


class LeavePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #locatos

        self.titre_leave_page = page.locator("h6.oxd-text--h6", has_text="Leave")
        self.menu_apply = page.locator(".oxd-topbar-body-nav-tab-item", has_text="Apply")

    #methodes

    def verifier_redirection_vers_LEAVE_page(self):
        self.verifier_element_visible(self.titre_leave_page)

    def cliquer_sur_apply(self):
        self.cliquer_sur_un_element(self.menu_apply)
