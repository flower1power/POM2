import allure
from selenium.webdriver.remote.webelement import WebElement

from base.base_page import BasePage
from data.urls import Urls


class DashboardPage(BasePage):
    _PAGE_URL = Urls.DASHBOARD_URL

    _WIDGET = ("xpath", "//div[contains(@class, 'orangehrm-dashboard-widget') and contains(@class, 'oxd-grid-item')]")

    def open(self):
        with allure.step(f"Открытие страницы {self._PAGE_URL}"):
            self._driver.get(self._PAGE_URL)

    def get_count_widget(self) -> int:
        return len(self._widgets)

    @property
    def _widgets(self) -> list[WebElement]:
        return self._wait.until(
            self._EC.visibility_of_all_elements_located(self._WIDGET),
            message="Не дождались появления виджетов",
        )
