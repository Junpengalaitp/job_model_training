import logging

from sqlalchemy import create_engine

from config.read_config import get_config
from logger.logger import setup_logging

SERVER_IP = get_config('SQL_SERVER', 'ip')
PORT = get_config('SQL_SERVER', 'port')
DB_NAME = get_config('SQL_SERVER', 'dbname')
username = get_config('SQL_SERVER', 'user')
password = get_config('SQL_SERVER', 'password')

conn = create_engine(
    f'postgresql://{username}:{password}@{SERVER_IP}:{PORT}/{DB_NAME}', pool_recycle=3600)

setup_logging()
logger = logging.getLogger("dbLogger")

