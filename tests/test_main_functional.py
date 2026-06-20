import allure

from page_objects.main_page import MainPage
from urls.main import MainUrl


@allure.suite("Тестирование основного функционала")
class TestMainFunctionality:

    @allure.title("Переход по нажатию на Конструктор")
    def test_click_on_constructor_section_success(self, browser):
        main_page = MainPage(browser)

        main_page.open_order_feed_page()
        main_page.click_on_constructor_section()

        assert main_page.get_current_url() == MainUrl.MAIN_PAGE_URL

    @allure.title("Переход по нажатию на Лента заказов")
    def test_click_on_order_feed_section_success(self, browser):
        main_page = MainPage(browser)

        main_page.open_home_page()
        main_page.click_on_order_feed_section()

        assert main_page.get_current_url() == MainUrl.ORDER_FEED_PAGE_URL

    @allure.title("По нажатию на ингредиент, появляется всплывающее окно с деталями ингредиента")
    def test_click_on_ingredient_item_opened_ingredient_detail_modal_success(self, browser):
        main_page = MainPage(browser)

        main_page.open_home_page()
        main_page.click_on_ingredient_item()

        assert main_page.is_opened_ingredient_detail_modal()

    @allure.title("Нажатием на крестик закрывается всплывающее окно с деталями ингредиента")
    def test_click_by_cross_closed_ingredient_detail_modal_success(self, browser):
        main_page = MainPage(browser)

        main_page.open_home_page()
        main_page.click_on_ingredient_item()
        main_page.is_opened_ingredient_detail_modal()
        main_page.click_close_ingredient_detail_modal()

        assert main_page.is_closed_ingredient_detail_modal()

    @allure.title("При добавлении ингредиента в заказ, счётчик этого ингредиента увеличивается")
    def test_add_ingredient_to_order_ingredient_count_is_increases_success(self, browser):
        main_page = MainPage(browser)

        main_page.open_home_page()
        main_page.add_ingredient_to_order()

        assert main_page.get_ingredient_count() == "2"