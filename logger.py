# Arquivo de configuração do logger

import logging
from common_codes import create_folder
import datetime

logger = logging.getLogger('main')

def config_log():
    date = datetime.datetime.now()
    format_date = date.strftime('%d') + '-' + date.strftime('%m') + '-' + date.strftime('%Y')
    create_folder('./logs')
    logging.basicConfig(
        filename=f'./logs/{format_date} log.log',
        level=logging.INFO,encoding='UTF-16',
        format="%(asctime)s | %(levelname)s: %(message)s"
    )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s: %(message)s"))
    logger.addHandler(console_handler)

config_log()