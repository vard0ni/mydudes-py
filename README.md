# MyDudes

Социальная сеть на Django

## Старт

##### 1) Сделать форк репозитория

##### 2) Клонировать репозиторий


#### 3) Создание виртуалки 
    python -m venv venv
    venv\Scripts\activate.bat - для Windows;
    source venv/bin/activate - для Linux и MacOS.

#### 4) Установка зависимостей
    pip install -r requirements.txt

#### 5) В корне проекта переименовать создать .env файл куда поместить следущие настройки:
    DEBUG=
    SECRET_KEY=
    DJANGO_ALLOWED_HOSTS=

    POSTGRES_DB=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_HOST=
    POSTGRES_PORT=

#### 6) Создание superuser'a 
    python manage.py createsuperuser

#### 7) Запуск сервера 
    python manage.py runserver


## Разработка с Docker
    ...