# 15_11_2023_test
Это выполненое задание:
https://docs.google.com/document/d/1fMFwPBs53xzcrltEFOpEG4GWTaQ-5jvVLrNT6_hmC7I/edit?usp=sharing

# Здравствуйте

## Все просто:
- Выполнено на Python 3.9
- По заданию требовалось использовать [tinyDB](https://tinydb.readthedocs.io/en/latest/intro.html)
  - Логика БД `web_form\form_app\tiny_models.py`
- Для работы:
  - Не забываем окружение и: `pip install -r requirements.txt` 
  - Рабочая директория: `15_11_2023_test`
  - Запустить тестовый сервер: `python web_form\manage.py runserver`
  - Прогнать тесты работы модели: `python -m unittest tests\test_tiny_models.py`
  - Для тестирования и визуализации запросов(сервер включон): `python  tests\test_tiny_api.py`
  - `dbdata\db.json` тестовая база, при желании можно заменить на свою, чтобы воссоздать: `python  dbdata\build_test_base.py`
  - В тестовой бд приняты названия в виде `TEPDtest`, где заглавные обозначают порядок и сокращенное название типов поля `T - text, E - email , P - phone, D -  date`
  - Имена полей в тестовой БД присваиваются `field_name_` + `порядковый номер` например `field_name_1`
  - `http://127.0.0.1:8000/api` наш тестовый адрес, благодаря djangorestframework можно использовать браузер для визуализации и тестов
  
#### Буду рад критике