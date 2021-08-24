#!/bin/sh
/bin/bash /app/commands/wait-for-it.sh "${DB_HOST}:${DB_PORT}" --timeout=90 --strict -- python manage.py migrate
python manage.py runserver 0.0.0.0:8000
