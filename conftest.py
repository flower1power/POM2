import os

import allure
import pytest
from selenium import webdriver


@pytest.fixture(autouse=True, scope="function")
def driver(request):
    try:
        browser = os.environ["BROWSER"]
    except KeyError:
        raise RuntimeError("Не установлена переменная окружения BROWSER. Пример: BROWSER=chrome pytest")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless=new")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Browser {browser} is not supported")

    driver.delete_all_cookies()
    request.cls.driver = driver

    yield driver

    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def allure_environment(request):
    allure_results_dir = request.config.getoption("--alluredir")
    if allure_results_dir:
        if not os.path.exists(allure_results_dir):
            os.makedirs(allure_results_dir)
        try:
            browser = os.environ["BROWSER"]
        except KeyError:
            raise RuntimeError("Не установлена переменная окружения BROWSER. Пример: BROWSER=chrome pytest")
        try:
            stage = os.environ["STAGE"]
        except KeyError:
            raise RuntimeError("Не установлена переменная окружения STAGE. Пример: STAGE=demo pytest")

        with open(os.path.join(allure_results_dir, "environment.properties"), "w") as f:
            f.write(f"Browser={browser}\n")
            f.write(f"STAGE={stage}\n")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        try:
            driver = item.cls.driver
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

            html = driver.page_source
            allure.attach(
                html,
                name="page_source.html",
                attachment_type=allure.attachment_type.HTML,
            )

            if hasattr(driver, 'get_log'):
                logs = driver.get_log("browser")
                if logs:
                    log_text = "\n".join([str(log) for log in logs])
                    allure.attach(
                        log_text,
                        name="browser_console.log",
                        attachment_type=allure.attachment_type.TEXT,
                    )
        except Exception as e:
            print(f"Failed to take screenshot or attach debug info: {e}")
