import multiprocessing
import os


bind = '0.0.0.0:' + os.environ.get('PORT', '8001')
max_requests = 1000
workers = (multiprocessing.cpu_count() * 2) + 1
env = {'DJANGO_SETTINGS_MODULE': 'SHRTN_engine.settings'}
reload = True

