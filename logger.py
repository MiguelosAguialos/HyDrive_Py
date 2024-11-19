import logging
import os
import datetime

logger = logging.getLogger('main')

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def config_log():
    date = datetime.datetime.now()
    format_date = date.strftime('%d') + '-' + date.strftime('%m') + '-' + date.strftime('%Y')
    create_folder('./logs')
    logging.basicConfig(
        filename=f'./logs/{format_date} log.log',
        level=logging.INFO,encoding='UTF-16',
        format="%(asctime)s | %(levelname)s: %(message)s"
    )

config_log()