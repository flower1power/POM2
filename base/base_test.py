from faker import Faker

from pages.auth_page import AuthPage
from pages.dashboard_page import DashboardPage
from pages.reset_password_page import ResetPasswordPage


class BaseTest:
    def setup_method(self):
        self.auth_page = lambda driver=self.driver: AuthPage(driver)
        self.reset_password_page = lambda driver=self.driver: ResetPasswordPage(driver)
        self.dashboard_page = lambda driver=self.driver: DashboardPage(driver)
        self.faker = Faker()
