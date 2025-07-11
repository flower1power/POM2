import allure
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.urls import Urls


class AuthPage:
    _PAGE_URL = Urls.AUTH_PAGE

    _BRANDING_LOCATOR = (
        "xpath",
        "//div[@class='orangehrm-login-branding']/img[@alt='company-branding']",
    )
    _LOGO_LOCATOR = (
        "xpath",
        "//div[@class='orangehrm-login-logo']/img[@alt='orangehrm-logo']",
    )
    _USERNAME_INPUT_LOCATOR = ("xpath", "//input[@name='username']")
    _PASSWORD_INPUT_LOCATOR = ("xpath", "//input[@name='password']")
    _LOGIN_BUTTON_LOCATOR = (
        "xpath",
        "//button[@type='submit' and normalize-space()='Login']",
    )
    _FORGOT_PASSWORD_LINK_LOCATOR = (
        "xpath",
        "//p[normalize-space()='Forgot your password?']",
    )
    _CREDENTIALS_ERROR_LOCATOR = (
        "xpath",
        "//div[contains(@class, 'oxd-alert-content--error')]/p[normalize-space()='Invalid credentials']",
    )

    def __init__(self, driver):
        self._driver: WebDriver = driver
        self._wait = WebDriverWait(self._driver, 10, 1)
        self._EC = expected_conditions

    def open(self):
        with allure.step(f"Открытие страницы: {self._PAGE_URL}"):
            self._driver.get(self._PAGE_URL)

    def fill_username(self, username: str):
        with allure.step(f"Заполнение username: {username}"):
            self._username_input.send_keys(username)

    def fill_password(self, password: str):
        with allure.step(f"Заполнение password: {password}"):
            self._password_input.send_keys(password)

    @allure.step("Клик по ссылке сброса пароля")
    def click_forgot_password(self):
        with allure.step("Клик по ссылке сброса пароля"):
            self._forgot_password_link.click()

    @allure.step("Клик по кнопке Login")
    def click_login_button(self):
        self._login_button.click()

    @allure.step("Авторизация пользователя")
    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()

    @allure.step("Получение текста ошибки")
    def get_credentials_error_text(self) -> str:
        return self._credentials_error.text

    @allure.step("Получение текста ссылки сброса пароля")
    def get_forgot_password_link_text(self) -> str:
        return self._forgot_password_link.text

    @allure.step("Проверка загрузки страницы")
    def is_loaded(self) -> bool:
        try:
            self._branding_img
            self._logo_img
            self._username_input
            self._password_input
            self._login_button
            self._forgot_password_link
            return True
        except TimeoutException:
            return False

    @property
    def _branding_img(self) -> WebElement:
        return self._wait.until(
            self._EC.visibility_of_element_located(self._BRANDING_LOCATOR)
        )

    @property
    def _logo_img(self) -> WebElement:
        return self._wait.until(
            self._EC.visibility_of_element_located(self._LOGO_LOCATOR)
        )

    @property
    def _username_input(self) -> WebElement:
        return self._wait.until(
            self._EC.visibility_of_element_located(self._USERNAME_INPUT_LOCATOR)
        )

    @property
    def _password_input(self) -> WebElement:
        return self._wait.until(
            self._EC.visibility_of_element_located(self._PASSWORD_INPUT_LOCATOR)
        )

    @property
    def _login_button(self) -> WebElement:
        return self._wait.until(
            self._EC.visibility_of_element_located(self._LOGIN_BUTTON_LOCATOR)
        )

    @property
    def _forgot_password_link(self) -> WebElement:
        return self._wait.until(
            self._EC.visibility_of_element_located(self._FORGOT_PASSWORD_LINK_LOCATOR)
        )

    @property
    def _credentials_error(self) -> WebElement:
        return self._wait.until(
            self._EC.visibility_of_element_located(self._CREDENTIALS_ERROR_LOCATOR)
        )
