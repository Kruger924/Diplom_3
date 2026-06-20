import pytest
from selenium import webdriver

from data.user import UserTestData
from page_objects.login_page import LoginPage


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    browsers = {
        "chrome": (webdriver.ChromeOptions, webdriver.Chrome),
        "firefox": (webdriver.FirefoxOptions, webdriver.Firefox),
    }

    browser_name = request.param
    if browser_name not in browsers:
        raise ValueError(
            f"Браузер {browser_name} не поддерживается, "
            f"список поддерживаемых браузеров: {browsers.keys()}"
        )

    options_cls, driver_cls = browsers.get(browser_name)

    options = options_cls()
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--headless')
    driver = driver_cls(options=options)
    driver.implicitly_wait(3)

    yield driver
    driver.quit()


@pytest.fixture
def auth_user(browser):
    login_page = LoginPage(browser)

    login_page.open_login_page()
    login_page.send_email(UserTestData.EMAIL)
    login_page.send_password(UserTestData.PASSWORD)
    login_page.click_login_btn()

    login_page.click_create_order_button()

    return browser