from enum import Enum


class NavMenuButton(str, Enum):
    ADMIN = "ADMIN_BUTTON"
    PIM = "PIM_BUTTON"
    TIME = "TIME_BUTTON"
    RECRUITMENT = "RECRUITMENT_BUTTON"
    MY_INFO = "MY_INFO_BUTTON"
    PERFORMANCE = "PERFORMANCE_BUTTON"
    DASHBOARD = "DASHBOARD_BUTTON"
    DIRECTORY = "DIRECTORY_BUTTON"
    MAINTENANCE = "MAINTENANCE_BUTTON"
    CLAIM = "CLAIM_BUTTON"
    BUZZ = "BUZZ_BUTTON"


class DropDownItems(str, Enum):
    ABOUT = "ABOUT"
    SUPPORT = "SUPPORT"
    CHANGE_PASSWORD = "CHANGE_PASSWORD"
    LOGOUT = "LOGOUT"
