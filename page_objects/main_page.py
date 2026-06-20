import allure

from locators.main import (
    CONSTRUCTOR_BASKET,
    CONSTRUCTOR_SECTION,
    CLOSE_INGREDIENT_INFO_BTN,
    INGREDIENT_COUNTER,
    INGREDIENT_DETAIL_MODAL,
    INGREDIENT_ITEM,
    ORDER_FEED_SECTION
)
from page_objects.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Переход в раздел Конструктор")
    def click_on_constructor_section(self):
        self.click_item(CONSTRUCTOR_SECTION)

    @allure.step("Переход в раздел Лента заказов")
    def click_on_order_feed_section(self):
        self.click_item(ORDER_FEED_SECTION)

    @allure.step("Нажатие на ингредиент")
    def click_on_ingredient_item(self):
        self.click_item(INGREDIENT_ITEM)

    @allure.step("Появление всплывающего окна с деталями ингредиента")
    def is_opened_ingredient_detail_modal(self):
        return self.wait_for_element(INGREDIENT_DETAIL_MODAL)

    @allure.step("Закрыть всплывающее окно деталей ингредиента")
    def click_close_ingredient_detail_modal(self):
        self.click_item(CLOSE_INGREDIENT_INFO_BTN)

    @allure.step("Появление всплывающего окна с деталями ингредиента")
    def is_closed_ingredient_detail_modal(self):
        return self.wait_for_invisibility_of_element(INGREDIENT_DETAIL_MODAL)

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_to_order(self):
        self.drag_and_drop(
            self.find(INGREDIENT_ITEM),
            self.find(CONSTRUCTOR_BASKET)
        )

    @allure.step("Получить количество ингредиентов в заказе")
    def get_ingredient_count(self):
        return self.get_text(INGREDIENT_COUNTER)