import allure

from locators.order import (
    ALL_ORDERS_DONE_TEXT,
    COMPLETED_ORDERS_COUNT_ALL_THE_TIME,
    COMPLETED_ORDERS_COUNT_TODAY
)
from page_objects.order_page import OrderFeedPage


@allure.suite("Лента заказов")
class TestOrderFeed:

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_create_new_order_show_in_processing_success(self, auth_user):
        order_page = OrderFeedPage(auth_user)

        new_order_num = order_page.create_order()
        order_page.open_order_feed_page()
        order_page.wait_for_invisibility_of_element(ALL_ORDERS_DONE_TEXT)
        order_page.open_order_feed_page()

        assert new_order_num in order_page.get_in_processing_order_numbers()

    @allure.title("При создании нового заказа счётчик За всё время увеличивается")
    def test_create_new_order_all_the_time_orders_count_is_increases_success(self, auth_user):
        order_page = OrderFeedPage(auth_user)

        order_page.open_order_feed_page()
        before_all_time_order = order_page.get_text(COMPLETED_ORDERS_COUNT_ALL_THE_TIME)

        order_page.create_order()
        order_page.click_close_place_order()

        order_page.open_order_feed_page()
        after_all_time_order = order_page.get_text(COMPLETED_ORDERS_COUNT_ALL_THE_TIME)

        assert int(after_all_time_order) > int(before_all_time_order)

    @allure.title("При создании нового заказа счётчик За сегодня увеличивается")
    def test_create_new_order_for_today_orders_count_is_increases_success(self, auth_user):
        order_feed_page = OrderFeedPage(auth_user)

        order_feed_page.open_order_feed_page()
        before_for_today_order = order_feed_page.get_text(COMPLETED_ORDERS_COUNT_TODAY)

        order_feed_page.create_order()
        order_feed_page.click_close_place_order()

        order_feed_page.open_order_feed_page()
        after_for_today_order = order_feed_page.get_text(COMPLETED_ORDERS_COUNT_TODAY)

        assert int(after_for_today_order) > int(before_for_today_order)