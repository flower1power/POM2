import allure
import pytest

from base.base_test import BaseTest
from base.enums.base_page_enums import DropDownItems, NavMenuButton
from data.credential import Credential

navigate_parameters = [
    (NavMenuButton.ADMIN, "Admin"),
    (NavMenuButton.PIM, "PIM"),
    (NavMenuButton.TIME, "Time"),
    (NavMenuButton.RECRUITMENT, "Recruitment"),
    (NavMenuButton.MY_INFO, "My info"),  # баг отображается PIM
    (NavMenuButton.PERFORMANCE, "Performance"),
    (NavMenuButton.DASHBOARD, "Dashboard"),
    (NavMenuButton.DIRECTORY, "Directory"),
    (NavMenuButton.CLAIM, "Claim"),
    (NavMenuButton.BUZZ, "Buzz"),
]


@allure.epic("Навигация")
class TestNavigate(BaseTest):

    @allure.title("Вход на dashboard_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_dashboard_page(self):
        self.auth_page.open()
        self.auth_page.login(Credential.USERNAME, Credential.PASSWORD)
        assert self.dashboard_page.is_loaded(), "Не удалось зайти на dashboard_page"

    @allure.title("Выход из профиля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout(self):
        self.auth_page.open()
        self.auth_page.login(Credential.USERNAME, Credential.PASSWORD)
        self.dashboard_page.click_dropdown_items(DropDownItems.LOGOUT)
        assert self.auth_page.is_loaded(), "Не удалось выйти из профиля"

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("button, breadcrumb_text", navigate_parameters)
    @allure.title("Переход на страницу {button} через nav_bar")
    def test_navigate_by_nav_bar(self, button, breadcrumb_text):
        self.auth_page.open()
        self.auth_page.login(Credential.USERNAME, Credential.PASSWORD)
        self.dashboard_page.click_nav_menu_button(button)
        text = self.dashboard_page.get_header_breadcrumb_text()
        assert text.startswith(breadcrumb_text), f"Полученный текст {text} не соответствует ожидаемому {breadcrumb_text}"
