from celery import Celery

cerely_app = Celery('tasks', broker='pyamqp://guest@localhost//')


@cerely_app.task
def add_two_numbrs(x, y):
    return x + y

