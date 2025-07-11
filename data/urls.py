import os

from dotenv import load_dotenv

load_dotenv()

stages = {
	"dev" : "https://opensource-dev.orangehrmlive.com/web/index.php",
	"demo": "https://opensource-demo.orangehrmlive.com/web/index.php",
}

try:
    HOST = stages[os.environ["STAGE"]]
except KeyError:
    raise RuntimeError("Не установлена переменная окружения STAGE. Пример: STAGE=demo pytest")



class Urls:
	AUTH_PAGE = f"{HOST}/auth/login"
	DASHBOARD_URL = f"{HOST}/dashboard/index"
	RESET_PASSWORD_PAGE = f"{HOST}/auth/requestPasswordResetCode"
