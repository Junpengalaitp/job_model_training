from sqlalchemy import create_engine

from config.settings import SQL_IP, DB_PORT, DB_NAME, USERNAME, PASSWORD

SERVER_IP = SQL_IP
PORT = DB_PORT
db_name = DB_NAME
username = USERNAME
password = PASSWORD

conn = create_engine(f'postgresql://{username}:{password}@{SERVER_IP}:{PORT}/{DB_NAME}', pool_recycle=3600)


