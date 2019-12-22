import pandas as pd
from sqlalchemy import create_engine

from config.read_config import get_config

SERVER_IP = get_config('mysql', 'ip')
PORT = get_config('mysql', 'port')
DB_NAME = get_config('mysql', 'dbname')
username = get_config('mysql', 'user')
password = get_config('mysql', 'password')

conn = create_engine(
    f'mysql+mysqlconnector://{username}:{password}@{SERVER_IP}:{PORT}/{DB_NAME}?charset=utf8', pool_recycle=3600)


def select_raw_words() -> pd.DataFrame:
    sql_query = """
                    SELECT * FROM keywords_en_core_web_lg
                """
    return pd.read_sql_query(sql_query, conn)


def select_job_model_words() -> pd.DataFrame:
    sql_query = """
                    SELECT * FROM keywords_job_model
                """
    return pd.read_sql_query(sql_query, conn)


if __name__ == '__main__':
    df = select_job_model_words()
    print(df)
