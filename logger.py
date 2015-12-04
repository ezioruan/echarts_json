# -*- coding: utf-8 -*-
import logging
import sys
from logging.handlers import TimedRotatingFileHandler
from setting import LOG_DIR
import os

file_name = os.path.join(LOG_DIR, "echarts_json")


log = logging.getLogger('echarts_json')
formater = logging.Formatter('%(asctime)s - %(message)s', '%m-%d %H:%M:%S')
log.setLevel(logging.DEBUG)
f1 = TimedRotatingFileHandler(file_name, 'midnight')
f1.setFormatter(formater)
console = logging.StreamHandler(sys.stdout)
console.setFormatter(formater)

log.addHandler(console)
log.addHandler(f1)
