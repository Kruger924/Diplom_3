import allure
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core.constants.js import DRAG_AND_DROP
from core.constants import BASE_URL
from locators.base import LOADER_MODAL
from locators.order import CREATE_ORDER_BTN
from urls.main import MainUrl


class BasePage:
    def __init__(self, driver, timeout=45):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть URL: {url}")
    def open_url(self, url):
        self.driver.get(url)
        self.wait_for_invisibility_of_element(LOADER_MODAL)

    @allure.step("Открыть Главную страницу")
    def open_home_page(self):
        self.open_url(BASE_URL)

    @allure.step("Открыть Ленту Заказов")
    def open_order_feed_page(self):
        self.open_url(MainUrl.ORDER_FEED_PAGE_URL)

    @allure.step("Ожидание условия")
    def wait_until(self, func, timeout=45):
        return WebDriverWait(self.driver, timeout).until(func)

    @allure.step("Ожидать появление '{locator}'")
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидать исчезновение '{locator}'")
    def wait_for_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver, 45).until(EC.invisibility_of_element_located(locator))

    @allure.step("Нажатие на '{locator}'")
    def click_item(self, locator):
        try:
            elem = self.wait.until(EC.element_to_be_clickable(locator))
            elem.click()
        except ElementClickInterceptedException:
            elem = self.wait.until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", elem)

    @allure.step("Найти '{locator}'")
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Нажатие на кнопку Оформить заказ")
    def click_create_order_button(self):
        self.click_item(CREATE_ORDER_BTN)

    @allure.step("Получить кликабельный элемент")
    def get_clickable_element(self, locator):
        WebDriverWait(self.driver, 45).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step("Получить текст")
    def get_text(self, locator):
        return self.get_clickable_element(locator).text

    @allure.step("Получить URL текущей страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Перетаскивание ингредиента в заказ")
    def drag_and_drop(self, element, target):
        self.driver.execute_script(DRAG_AND_DROP, element, target)