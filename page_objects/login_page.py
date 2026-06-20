import allure

from locators.base import LOADER_MODAL
from locators.login import EMAIL_INPUT, LOGIN_BTN, PASSWORD_INPUT
from page_objects.base_page import BasePage
from urls.auth import AuthUrl


class LoginPage(BasePage):

    @allure.step("Открыть страницу авторизации")
    def open_login_page(self):
        self.driver.get(AuthUrl.LOGIN_PAGE_URL)
        self.wait_for_invisibility_of_element(LOADER_MODAL)

    @allure.step("Нажать на Войти")
    def click_login_btn(self):
        self.get_clickable_element(LOGIN_BTN).click()

    @allure.step("Заполнить поле Email: {email}")
    def send_email(self, email):
        self.get_clickable_element(EMAIL_INPUT).send_keys(email)

    @allure.step("Заполнить поле Пароль")
    def send_password(self, password):
        self.get_clickable_element(PASSWORD_INPUT).send_keys(password)