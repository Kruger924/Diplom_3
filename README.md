# Diplom_3 UI-тестирование

В данном проекте тестировалась функциональность UI интерфейса для Stellar Burgers с помощью Selenium для браузеров Google Chrome и Mozilla Firefox.
URL стенда: https://stellarburgers.education-services.ru/

1. Установить браузеры Google Chrome, Mozilla Firefox и драйвер Selenium
2. Установить зависимости: pip install -r requirements.txt
3. Для запуска тестов из директории tests необходимо выполнить команду: pytest tests --alluredir=allure_results
4. Посмотреть отчет выполненных тестов: allure serve allure_results