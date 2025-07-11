# POM: Page Object Model для автоматизации тестирования

---

## Структура проекта

```
POM2/
│
├── base/                # Базовые классы для страниц и тестов
│   ├── base_page.py
│   ├── base_test.py
│   └── enums/
│       └── base_page_enums.py
│
├── pages/               # Page Object классы для различных страниц приложения
│   ├── auth_page.py
│   ├── dashboard_page.py
│   └── reset_password_page.py
│
├── data/                # Тестовые данные и вспомогательные модули
│   ├── credential.py
│   └── urls.py
│
├── tests/               # Тестовые сценарии
│   ├── test_login.py
│   └── test_navigate.py
│
├── conftest.py          # Фикстуры Pytest
├── pytest.ini           # Конфигурация Pytest
├── requirements.txt     # Зависимости проекта
└── README.md            # Документация
```

---

## Установка зависимостей

  ```bash
  pip install -r requirements.txt
  ```

---

## Пример запуска тестов

```bash
pytest --browser=chrome --stage=demo
pytest --browser=firefox --stage=dev
```

## Структура Page Object

- Все страницы реализованы в папке `pages/`.
- Базовые методы для работы с элементами вынесены в `BasePage` (`base/base_page.py`).
- Для добавления новой страницы:
  1. Создайте новый класс в `pages/`, по возможности унаследуйте от BasePage.
  2. Опишите локаторы и бизнес-методы.
- Для добавления нового теста:
  1. Создайте файл в `tests/`.
  2. Используйте Page Object и фикстуры.

## Логирование и отладка

- Все шаги тестов логируются через Allure steps.
- При падении теста в Allure автоматически прикладываются:
  - Скриншот страницы
  - HTML-код страницы
  - Логи браузера (console logs)
- Для просмотра отчёта:
  ```bash
  allure generate allure-results -o allure-report --clean
  allure open ./allure-report
  ```

## Переменные окружения

- Все чувствительные данные (логин, пароль, стенд) задаются через переменные окружения или файл `.env`.
- Пример файла см. в `.env.example`.
