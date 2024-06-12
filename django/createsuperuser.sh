#!/bin/sh

export DJANGO_SUPERUSER_PASSWORD=admin
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@admin.aa

python manage.py createsuperuser --noinput -v 3 --traceback
