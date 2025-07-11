from faker import Faker

from pages.auth_page import AuthPage
from pages.dashboard_page import DashboardPage
from pages.reset_password_page import ResetPasswordPage


class BaseTest:
    def setup_method(self):
        self.auth_page = AuthPage(self.driver)
        self.reset_password_page = ResetPasswordPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.faker = Faker()
