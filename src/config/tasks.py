from __future__ import absolute_import, unicode_literals
import time

from celery import Celery

celery_app = Celery('tasks')
# CELERY_がプレフィックスになっている設定を読み込む。
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

@celery_app.task
def add(x, y):
    time.sleep(10)
    return x + y