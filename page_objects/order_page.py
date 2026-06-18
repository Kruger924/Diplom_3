import allure

from locators.base import LOADER_MODAL
from locators.main import CONSTRUCTOR_BASKET, INGREDIENT_ITEM
from locators.order import (
    ALL_ORDERS_NUMBER_IN_PROCESS_MODAL,
    CREATE_ORDER_BTN,
    IN_PROCESSING_ORDER_ITEMS,
    ORDER_NUMBER_IN_MODAL_TEXT,
    ORDER_STARTED_MODAL_CLOSE_BTN
)
from page_objects.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Нажать Оформить заказ")
    def click_place_order(self):
        self.click_item(CREATE_ORDER_BTN)

    @allure.step("Закрытие всплывающего окна Заказ создан")
    def click_close_place_order(self):
        self.click_item(ORDER_STARTED_MODAL_CLOSE_BTN)

    @allure.step("Перенос ингредиента в Заказ")
    def move_ingredient_to_order(self):
        self.drag_and_drop(
            self.find(INGREDIENT_ITEM),
            self.find(CONSTRUCTOR_BASKET)
        )

    def get_in_processing_order_numbers(self):
        ul_elem = self.find(ALL_ORDERS_NUMBER_IN_PROCESS_MODAL)
        return [
            li.text.strip()
            for li in ul_elem.find_elements(*IN_PROCESSING_ORDER_ITEMS)
        ]

    def wait_for_real_order_number(self, timeout=20):
        def is_real_order_number(_):
            text = self.find(ORDER_NUMBER_IN_MODAL_TEXT).text.strip()
            return text.isdigit() and text != "9999"

        self.wait_until(is_real_order_number, timeout)

        return self.find(ORDER_NUMBER_IN_MODAL_TEXT).text.strip().zfill(7)

    @allure.step("Создание заказа")
    def create_order(self):
        self.open_home_page()
        self.move_ingredient_to_order()
        self.click_place_order()

        self.wait_for_invisibility_of_element(LOADER_MODAL)

        order_number = self.wait_for_real_order_number()
        self.click_close_place_order()

        return order_number