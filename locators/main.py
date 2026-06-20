from selenium.webdriver.common.by import By

# Раздел Конструктор
CONSTRUCTOR_SECTION = (By.XPATH, '//*[contains(text(),"Конструктор")]')

# Раздел Лента заказов
ORDER_FEED_SECTION = (By.XPATH, '//a[@href="/feed"]')

# Элемент ингредиента
INGREDIENT_ITEM = (By.XPATH, '//*[contains(@class,"BurgerIngredient_ingredient__")]')

# Кнопка Закрыть детали ингредиента
CLOSE_INGREDIENT_INFO_BTN = (
    By.XPATH,
    '//h2[contains(text(),"Детали ингредиента")]/..//..//button[contains(@class,"Modal_modal__close")]'
)

# Детали ингредиента
INGREDIENT_DETAIL_MODAL = (By.XPATH, '//h2[contains(text(),"Детали ингредиента")]')

# Пространство сбора заказа
CONSTRUCTOR_BASKET = (By.XPATH, '//ul[contains(@class,"BurgerConstructor_basket")]')

# Счётчик ингредиента
INGREDIENT_COUNTER = (
    By.XPATH,
    '//*[contains(@class,"BurgerIngredient_ingredient__")]//*[contains(@class,"counter_default__")]'
)