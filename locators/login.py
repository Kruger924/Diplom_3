from selenium.webdriver.common.by import By

# Кнопка Войти
LOGIN_BTN = (By.XPATH, '//button[text()="Войти"]')

# Поле ввода Email
EMAIL_INPUT = (By.XPATH, '//*[contains(text(),"Email")]/parent::*/input')

# Поле ввода Пароль
PASSWORD_INPUT = (By.XPATH, '//*[contains(text(),"Пароль")]/parent::*/input')