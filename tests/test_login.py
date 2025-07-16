import time

import allure

from base.base_test import BaseTest
from data.credential import Credential


@allure.epic("Login page")
class TestLogin(BaseTest):

    @allure.title("Успешный вход в систему")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_success_login(self):
        self.auth_page().open()
        self.auth_page().login(Credential.USERNAME, Credential.PASSWORD)
        assert self.dashboard_page().is_loaded(), "Не удалось зайти на dashboard_page"
        time.sleep(5)

    @allure.title("Неудачный вход в систему")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_failed_login(self):
        self.auth_page().open()
        self.auth_page().login(self.faker.user_name(), self.faker.password())
        assert self.auth_page().get_credentials_error_text() == "Invalid credentials"

    @allure.title("Переход на страницу сброса пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_reset_page(self):
        self.auth_page().open()
        self.auth_page().click_forgot_password()
        assert self.reset_password_page().is_loaded(), "Не удалось перейти на страницу сброса пароля"
