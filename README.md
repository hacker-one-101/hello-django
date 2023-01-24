# Задание

Написать ansible плейбуки для деплоя django приложения.

Должны быть отдельные плейбуки для:
- подготовки окружения (установка nginx, mysql, python и т.д)
- деплоя приложения

Во время деплоя необходимо:
- установить зависимости из requirements.txt
- обновить конфиг прилжения
- выполнить миграцию бд
- выполнить сборку статичных файлов
- перезапустить приложение

# Запуск проекта
- создать продакшен конфиг `settings_prod.py`, положить рядом с `hello_django/settings_dev.py`
- в конфиге (взять за образец `hello_django/settings_dev.py`) переопределить настройки для подключения к БД(`DATABASES`) и расположение статичных файлов(`STATIC_ROOT`)
- для запуска приложения и скриптов необходимо проставить переменную окружения `DJANGO_SETTINGS_MODULE=hello_django.settings_prod`
- выполнить миграцию БД: `./manage.py migrate`
- выполнить сборку статики: `./manage.py collectstatic`, после этой команды по пути указанном в STATIC_ROOT появятся статичные файлы
- запустить сервер: `gunicorn hello_django.wsgi --bind=0.0.0.0:8086`

