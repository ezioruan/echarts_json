# -*- coding : utf8 -*-
import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
LOG_DIR = os.path.join(ROOT_DIR, 'logs')
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)
SQL_LOG_ERROR_FILE = os.path.join(LOG_DIR, 'sql_error.log')


DB_HOST = '222.76.217.52'
DB_USER = 'lim'
DB_PORT = 1433
DB_PASSWORD = '123456x'
DB_DATABASE = 'test'
DB_CHARSET = 'utf8'

