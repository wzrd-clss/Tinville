web: newrelic-admin run-program gunicorn Tinville.wsgi --worker-class gevent --worker-connections 20 --log-file -
worker: python manage.py celery worker -B -l info