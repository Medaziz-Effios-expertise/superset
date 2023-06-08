source venv/bin/activate
celery --app=superset.tasks.celery_app:app worker --pool=prefork -O fair -c 1
