#!/bin/sh

# from https://www.caktusgroup.com/blog/2017/03/14/production-ready-dockerfile-your-python-django-app/
# entrypoint design

set -e

until python manage.py db_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing"

sleep 5

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    python manage.py migrate --noinput
fi

if [ "x$DJANGO_MANAGEPY_COLLECTSTATIC" = 'xon' ]; then
    python manage.py collectstatic --noinput -i *.scss -i /app/curriculum_platform/static/css/gmri-bootstrap
fi

chown -R uwsgi:uwsgi /static

exec "$@"
