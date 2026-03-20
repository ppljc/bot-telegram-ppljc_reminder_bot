# Python модули
from dotenv import load_dotenv

import os


# Чтение переменных окружения из .env файла
load_dotenv(override=True)

BOT_TOKEN = os.environ['BOT_TOKEN']
JSON_FILE = os.environ['JSON_FILE']
PROXY_SCHEME = os.environ['PROXY_SCHEME']
PROXY_HOSTNAME = os.environ['PROXY_HOSTNAME']
PROXY_PORT = int(os.environ['PROXY_PORT'])
PROXY_LOGIN = os.environ['PROXY_LOGIN']
PROXY_PASSWORD = os.environ['PROXY_PASSWORD']
