#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py makemigrations customer landing shop artisan
python manage.py migrate