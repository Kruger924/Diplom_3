from helpers.auth_user_page import AuthUserPage
from helpers.main_page import MainPage
from helpers.create_order_page import CreateOrderPage



class UIWorkerWeb(MainPage, AuthUserPage, CreateOrderPage):
    """Класс объединяет все классы по работе со страницами используя множественно наследование"""
    def __init__(self, driver, locators):
        super().__init__(driver)
        self.locators = locators