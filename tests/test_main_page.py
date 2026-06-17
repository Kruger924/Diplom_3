import time
import allure
import pytest

from data.urls import Urls


class TestMainPage:

    @allure.title('При нажатии кнопки Конструктор совершается переход на старницу сбора бургера')
    @allure.description('При нажатии кнопки Конструктор  происходит переход на страницу сбора бургера')
    def test_go_to_constructor(self, pages):
        pages.click_orders_list_button()
        pages.click_constructor_button()
        current_url = pages.get_current_url()
        assert current_url == Urls.url_main

    @allure.title('При нажатии кнопки Лента заказов совершается переход на страницу заказов')
    @allure.description('При нажатии кнопки Лента заказов происходит переход на страницу с заказами')
    def test_redirection_to_order_list(self, pages):
        pages.click_orders_list_button()
        current_url = pages.get_current_url()
        assert current_url == Urls.url_feed

    
    @allure.title('При нажатии на ингредиент всплывает окно с деталями')
    @allure.description('При нажатии на ингредиент всплывает модальное окно с информацией об ингредиенте')
    def test_popup_of_ingredient(self, pages):
        pages.click_on_ingredient()
        actually_text = pages.check_show_window_with_details()
        assert actually_text == "Детали ингредиента"

    @allure.title('Всплывающее окно с информацией об ингридиенте закрывается при нажатии на крестик')
    @allure.description('Нажимаем на крестик в правом верхнем углу окна и проверяем, что всплывающее окно закрылось')
    def test_close_ingredient_details_window(self, pages):
        pages.click_on_ingredient()
        pages.click_cross_button()
        pages.invisibility_ingredient_details()
        assert pages.check_displayed_ingredient_details() == False

    @allure.title('При добавлении ингредиента в заказ, счетчик увеличивается')
    @allure.description('Проверяем что после добавления ингредиента счетчик ингредента увеличивается')
    def test_ingredient_counter(self, pages):
        prev_counter_value = pages.get_count_value()
        pages.add_filling_to_order()
        actual_value = pages.get_count_value()
        assert actual_value > prev_counter_value

    @allure.title('Проверка возможности оформления заказ авторизованным пользователем')
    @allure.description('Нажимаем кнопку Оформить заказ и проверяем, что заказ оформлен и появился идентификатор заказа')
    def test_successful_order(self, pages, login):
        pages.add_filling_to_order()
        pages.click_order_button()
        actually_text = pages.check_show_window_with_order_id()
        assert actually_text == "идентификатор заказа" and pages.check_displayed_order_status_text() == True