import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.enums.base_page_enums import DropDownItems, NavMenuButton
from data.urls import Urls


class BasePage:
    _PAGE_URL = Urls.DASHBOARD_URL

    _HEADER_BREADCRUMB_LOCATOR = ("xpath",
                                    "//div[@class='oxd-topbar-header']//h6[contains(@class, 'breadcrumb-module')]")
    _UPGRADE_BUTTON_LOCATOR = ("xpath", "//button[contains(@class, 'orangehrm-upgrade-button')]")
    _USER_NAME_BUTTON = ("xpath", "//p[@class='oxd-userdropdown-name']")
    _USER_DROPDOWN_MENU = ("xpath", "//ul[@class='oxd-dropdown-menu' and @role='menu']")

    _DROPDOWN_ITEMS: dict[DropDownItems, tuple[str, str]] = {
        DropDownItems.ABOUT: ("xpath", "//a[@class='oxd-userdropdown-link' and @role='menuitem' and text()='About']"),
        DropDownItems.SUPPORT: ("xpath",
                                "//a[@class='oxd-userdropdown-link' and @role='menuitem' and text()='Support']"),
        DropDownItems.CHANGE_PASSWORD: ("xpath",
                                        "//a[@class='oxd-userdropdown-link' and @role='menuitem' and text()='Change Password']"),
        DropDownItems.LOGOUT: ("xpath", "//a[@class='oxd-userdropdown-link' and @role='menuitem' and text()='Logout']")
    }

    _NAV_BAR = ("xpath", "//nav[@class='oxd-navbar-nav' and @role='navigation' and @aria-label='Sidepanel']")
    _HIDE_NAV_BAR_BUTTON = ("xpath", "//button[@role='none']")
    _LOGO = ("xpath", "//div[@class='oxd-brand-banner']/img[@alt='client brand banner']")
    _SEARCH_INPUT = ("xpath", "//input[@placeholder='Search']")

    _NAV_MENU_BUTTONS: dict[NavMenuButton, tuple[str, str]] = {
        NavMenuButton.ADMIN: ("xpath", ".//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Admin']"),
        NavMenuButton.PIM: ("xpath", ".//a[contains(@class, 'oxd-main-menu-item')]/span[text()='PIM']"),
        NavMenuButton.TIME: ("xpath", ".//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Time']"),
        NavMenuButton.RECRUITMENT: ("xpath", ".//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Recruitment']"),
        NavMenuButton.MY_INFO: ("xpath", ".//a[contains(@class, 'oxd-main-menu-item')]/span[text()='My Info']"),
        NavMenuButton.PERFORMANCE: ("xpath", ".a[contains(@class, 'oxd-main-menu-item')]/span[text()='Performance']"),
        NavMenuButton.DASHBOARD: ("xpath", ".//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Dashboard']"),
        NavMenuButton.DIRECTORY: ("xpath", ".//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Directory']"),
        NavMenuButton.MAINTENANCE: ("xpath", ".//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Maintenance']"),
        NavMenuButton.CLAIM: ("xpath", ".//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Claim']"),
        NavMenuButton.BUZZ: ("xpath", ".//a[contains(@class, 'oxd-main-menu-item')]/span[text()='Buzz']")
    }

    def __init__(self, driver):
        self._driver: WebDriver = driver
        self._wait = WebDriverWait(self._driver, 10, 1)
        self._EC = expected_conditions


    def open(self):
        with allure.step(f"Открытие страницы: {self._PAGE_URL}"):
            self._driver.get(self._PAGE_URL)

    @allure.step("Клик на кнопку Upgrade")
    def click_upgrade_btn(self):
        self._upgrade_btn.click()

    @allure.step("Клик на кнопку Username")
    def click_username_btn(self):
        self._username_btn.click()

    def click_dropdown_items(self, name_btn: DropDownItems):
        with allure.step(f"Клик на элемент меню пользователя: {name_btn}"):
            self.click_username_btn()
            self._username_dropdown_menu
            by, value = self._DROPDOWN_ITEMS[name_btn]
            self._wait.until(
                self._EC.element_to_be_clickable((by, value))
            ).click()

    @allure.step("Скрытие меню")
    def hided_nav_bar(self):
        self._hide_nav_bar_btn.click()

    def search(self, text: str):
        with allure.step(f"Поиск: {text}"):
            search_input = self._search_input
            search_input.send_keys(text)
            search_input.send_keys(Keys.ENTER)

    def click_nav_menu_button(self, name_btn: NavMenuButton):
        with allure.step(f"Клик на кнопку меню навигации: {name_btn}"):
            nav_bar = self._nav_bar
            by, value = self._NAV_MENU_BUTTONS[name_btn]
            self._wait.until(
                self._EC.element_to_be_clickable(nav_bar.find_element(by, value))
            ).click()

    @allure.step("Проверка загрузки страницы")
    def is_loaded(self) -> bool:
        try:
            self._upgrade_btn
            self._username_btn
            self._nav_bar
            self._hide_nav_bar_btn
            self._logo
            self._search_input

            for button in self._NAV_MENU_BUTTONS.values():
                self._wait.until(self._EC.visibility_of_element_located(button))

            return True
        except TimeoutException:
            return False

    def get_header_breadcrumb_text(self) -> str:
        elements = self._wait.until(self._EC.visibility_of_all_elements_located(self._HEADER_BREADCRUMB_LOCATOR))
        result = []
        for element in elements:
            result.append(element.text)

        return "/".join(result)

    @property
    def _upgrade_btn(self) -> WebElement:
        return self._wait.until(self._EC.element_to_be_clickable(self._UPGRADE_BUTTON_LOCATOR))

    @property
    def _username_btn(self) -> WebElement:
        return self._wait.until(self._EC.element_to_be_clickable(self._USER_NAME_BUTTON))

    @property
    def _username_dropdown_menu(self) -> WebElement:
        return self._wait.until(self._EC.element_to_be_clickable(self._USER_DROPDOWN_MENU))

    @property
    def _nav_bar(self) -> WebElement:
        return self._wait.until(self._EC.visibility_of_element_located(self._NAV_BAR))

    @property
    def _hide_nav_bar_btn(self) -> WebElement:
        return self._wait.until(self._EC.element_to_be_clickable(self._HIDE_NAV_BAR_BUTTON))

    @property
    def _logo(self) -> WebElement:
        return self._wait.until(self._EC.visibility_of_element_located(self._LOGO))

    @property
    def _search_input(self) -> WebElement:
        return self._wait.until(self._EC.element_to_be_clickable(self._SEARCH_INPUT))

