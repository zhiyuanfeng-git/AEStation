""" Wrapping process environment variables.
"""

import os
from dotenv import load_dotenv
from django.core.management.utils import get_random_secret_key

DEBUG = True

load_dotenv() # take environment variables from .env


SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = get_random_secret_key()

DB_ENGINE_NAME = os.getenv('DB_ENGINE_NAME')

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# default configurations for mysql
if DB_ENGINE_NAME == 'mysql':
    if not DB_NAME:
        DB_NAME = 'AEStation'
    if not DB_HOST:
        DB_HOST = '127.0.0.1'
    if not DB_PORT:
        DB_PORT = '3306'

