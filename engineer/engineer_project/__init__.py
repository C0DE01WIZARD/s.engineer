# django_celery/__init__.py

from engineer_project.celery import app as celery_app

__all__ = ("celery_app",) # для старта Celery_app