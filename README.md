
# Система оплаты

### Описание
Приложение позволяет производить выбор и оплату товара на сайте с помощью платежной карты. 


### Технологии
Python 3.11 \
Django 4.2 \
Stripe

### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
```
python -m venv venv
```
- Активируйте виртуальное окружение
```
source .venv/bin/activate
```
###### команда для Windows:
```
source venv/scripts/activate
```

- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
- Создайте супер-пользователя:
```
python3 manage.py createsuperuser
```
###### команда для Windows:
```
python manage.py createsuperuser
```
- Запустите сервер разработки
```
python3 manage.py runserver
```
###### команда для Windows:
```
python manage.py runserver
```

#### Для использования приложения пройти по ссылке:
```
http://127.0.0.1:8000/
```
#### Для использования админ-панели приложения пройти по ссылке:
```
http://127.0.0.1:8000/admin/
```

### Авторы:
Максим