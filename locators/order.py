from selenium.webdriver.common.by import By

# Кнопка Оформить заказ
CREATE_ORDER_BTN = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')

# Информация о выполненных заказах Выполнено за всё время
COMPLETED_ORDERS_COUNT_ALL_THE_TIME = (
    By.XPATH,
    '//*[contains(text(),"Выполнено за все время")]/..//*[contains(@class,"OrderFeed_number__")]'
)

# Информация о выполненных заказах Выполнено за сегодня
COMPLETED_ORDERS_COUNT_TODAY = (
    By.XPATH,
    '//*[contains(text(),"Выполнено за сегодня")]/..//*[contains(@class,"OrderFeed_number__")]'
)

# Номер созданного заказа в всплывающем окне
ORDER_NUMBER_IN_MODAL_TEXT = (
    By.XPATH,
    ".//h2[contains(@class,'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m')]"
)

# Номера всех заказов в В работе
ALL_ORDERS_NUMBER_IN_PROCESS_MODAL = (
    By.XPATH,
    '//p[contains(text(),"В работе:")]/following-sibling::ul[1]'
)

# Текст Все текущие заказы готовы!
ALL_ORDERS_DONE_TEXT = (By.XPATH, '//*[contains(text(),"Все текущие заказы готовы!")]')

# Список всех заказов в В работе
IN_PROCESSING_ORDER_ITEMS = (By.XPATH, './/li')

# Всплывающее окно Заказ создан, Ваш заказ начали готовить
ORDER_STARTED_MODAL = (By.XPATH, '//*[contains(text(),"Ваш заказ начали готовить")]')

# Кнопка закрытия всплывающего окна Заказ создан
ORDER_STARTED_MODAL_CLOSE_BTN = (
    By.XPATH,
    '//*[contains(text(),"Ваш заказ начали готовить")]/..//..//..//button[contains(@class,"Modal_modal__close")]'
)