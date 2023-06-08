source venv/bin/activate
celery --app=superset.tasks.celery_app:app beat
