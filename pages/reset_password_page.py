import allure
from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement

from base.base_page import BasePage
from data.urls import Urls


class ResetPasswordPage(BasePage):
    _PAGE_URL = Urls.RESET_PASSWORD_PAGE

    _USERNAME_INPUT_LOCATOR = ("xpath", "//input[@name='username']")
    _CANCEL_BUTTON_LOCATOR = (
        "xpath",
        "//button[@type='button' and normalize-space()='Cancel']",
    )
    _REST_PASSWORD_BUTTON_LOCATOR = (
        "xpath",
        "//button[@type='submit' and normalize-space()='Reset Password' ]",
    )

    def fill_username(self, username: str):
        with allure.step(f"Заполнение инпута username: {username}"):
            self._username_input.send_keys(username)

    @allure.step("Клик на кнопку отмены")
    def click_cancel_btn(self):
        self._cancel_btn.click()

    @allure.step("Клик на кнопку сброса пароля")
    def click_reset_password_btn(self):
        self._reset_password_btn.click()

    @allure.step("Сброс пароля")
    def reset_password(self, username: str):
        self.fill_username(username)
        self.click_reset_password_btn()

    @allure.step("Получение текста из инпута username")
    def get_input_text(self) -> str:
        return self._username_input.text

    @allure.step("Проверка загрузки страницы")
    def is_loaded(self) -> bool:
        try:
            self._username_input
            self._cancel_btn
            self._reset_password_btn
            return True
        except TimeoutException:
            return False

    @property
    def _username_input(self) -> WebElement:
        return self._wait.until(
            self._EC.visibility_of_element_located(self._USERNAME_INPUT_LOCATOR),
            message="Не дождались появления инпута _USERNAME_INPUT_LOCATOR",
        )

    @property
    def _cancel_btn(self) -> WebElement:
        return self._wait.until(
            self._EC.visibility_of_element_located(self._CANCEL_BUTTON_LOCATOR),
            message="Не дождались появления кнопки _CANCEL_BUTTON_LOCATOR",
        )

    @property
    def _reset_password_btn(self) -> WebElement:
        return self._wait.until(
            self._EC.visibility_of_element_located(self._REST_PASSWORD_BUTTON_LOCATOR),
            message="Не дождались появления кнопки _REST_PASSWORD_BUTTON_LOCATOR",
        )
