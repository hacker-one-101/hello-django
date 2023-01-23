# запуск проекта
- создать продакшен конфиг settings_prod.py, положить рядом с hello_django/settings_dev.py
- export DJANGO_SETTINGS_MODULE=hello_django.settings_prod
- ./manage.py migrate
- ./manage.py collectstatic
- gunicorn hello_django.wsgi --bind=0.0.0.0:8086
