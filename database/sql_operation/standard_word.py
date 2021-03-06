import time
from datetime import datetime

import pandas as pd
import sqlalchemy
from loguru import logger

from database.sqlalchemy_manager import conn


def insert_standard_words(standard_word: str, other_words: str, category: str):
    query = f"""
                INSERT INTO standard_word (standard_word, other_words, category, modification_time) VALUES (
                '{standard_word}', '{other_words}', '{category}', '{datetime.now()}')
             """
    conn.execute(query)
    logger.info(f"insert success, standard_word: {standard_word}, other_words: {other_words}")


def update_stand_words(standard_word, other_words, category):
    query = f"""
                UPDATE standard_word
                SET other_words = '{other_words}', modification_time = '{datetime.now()}' , category = '{category}'
                WHERE standard_word = '{standard_word}'
             """
    conn.execute(query)
    logger.info(f"update success, standard_word: {standard_word}, other_words: {other_words}")


def delete_stand_word(standard_word):
    query = f"""
                DELETE FROM standard_word
                WHERE standard_word = '{standard_word}'
             """
    conn.execute(query)
    logger.info(f"delete success, standard_word: {standard_word}")


def select_standard_words(standard_word):
    query = f"""
                SELECT * FROM standard_word WHERE standard_word = '{standard_word}'
             """
    return pd.read_sql_query(query, conn)


def select_all_standard_words():
    query = f"""
                SELECT * FROM standard_word
             """
    return pd.read_sql_query(query, conn)


def select_by_job_id(db: str, job_id: str):
    query = f"""
                SELECT * FROM {db} where job_id = '{job_id}'
             """
    return pd.read_sql_query(query, conn)


def form_job_keyword_sql_params(job_df, df):
    if df is None:
        return
    result_list = []

    for index, row in df.iterrows():
        param_dict = {'keyword_name': row['keyword'], 'job_id': str(job_df['job_id']),
                      'created_time': time.strftime("%Y-%m-%d %H:%M:%S"), 'count': row['count'],
                      'source': 'dice', 'keyword_type': row['type'], "job_title": job_df["job_title"]}
        result_list.append(param_dict)
    return result_list


def insert_dice_job(job: dict):
    df = pd.DataFrame([job])
    df.to_sql("dice_job", if_exists='append', index=False, con=conn, dtype={
        'job_id': sqlalchemy.types.VARCHAR(length=255),
        'title': sqlalchemy.types.TEXT(),
        'company': sqlalchemy.types.VARCHAR(length=255),
        'location': sqlalchemy.types.VARCHAR(length=255),
        'tags': sqlalchemy.types.TEXT(),
        'category': sqlalchemy.types.VARCHAR(length=255),
        'job_desc': sqlalchemy.types.TEXT(),
        'raw_desc': sqlalchemy.types.TEXT(),
        'link': sqlalchemy.types.TEXT(),
        'source': sqlalchemy.types.VARCHAR(length=255),
        'state': sqlalchemy.types.VARCHAR(length=255),
        'salary': sqlalchemy.types.TEXT(),
        'employment_type': sqlalchemy.types.VARCHAR(length=255),
        'remote_available': sqlalchemy.types.VARCHAR(length=255),
        'job_date': sqlalchemy.types.VARCHAR(length=255),
        'crawled_time': sqlalchemy.types.DateTime(),
    })
    logger.info(f"insert success, id: {job['job_id']}")


def insert_remote_job(job: dict):
    df = pd.DataFrame([job])
    df.to_sql("remote_job", if_exists='append', index=False, con=conn, dtype={
        'job_id': sqlalchemy.types.VARCHAR(length=255),
        'title': sqlalchemy.types.TEXT(),
        'company': sqlalchemy.types.VARCHAR(length=255),
        'location': sqlalchemy.types.VARCHAR(length=255),
        'tags': sqlalchemy.types.TEXT(),
        'category': sqlalchemy.types.VARCHAR(length=255),
        'job_desc': sqlalchemy.types.TEXT(),
        'raw_desc': sqlalchemy.types.TEXT(),
        'link': sqlalchemy.types.TEXT(),
        'source': sqlalchemy.types.VARCHAR(length=255),
        'job_type': sqlalchemy.types.VARCHAR(length=255),
        'job_date': sqlalchemy.types.DateTime(),
        'crawled_time': sqlalchemy.types.DateTime(),
    })
    logger.info(f"insert success, id: {job['job_id']}")


def select_all_dice_jobs() -> pd.DataFrame:
    query = f"""
                SELECT job_id, title, job_desc FROM dice_job
             """
    return pd.read_sql_query(query, conn)


def insert_model_keywords(job_df: pd.DataFrame):
    job_df.to_sql("keywords_job_model", if_exists='append', index=False, con=conn, dtype={
        'keyword_name': sqlalchemy.types.VARCHAR(length=255),
        'standard_word': sqlalchemy.types.VARCHAR(length=255),
        'keyword_type': sqlalchemy.types.VARCHAR(length=255),
        'count': sqlalchemy.types.Integer(),
        'job_title': sqlalchemy.types.VARCHAR(length=255),
        'job_id': sqlalchemy.types.VARCHAR(length=255),
        'created_time': sqlalchemy.types.DateTime(),
        'source': sqlalchemy.types.VARCHAR(length=255),
    })


def select_all_model_keywords() -> pd.DataFrame:
    query = """
            SELECT DISTINCT keyword_name FROM keywords_job_model
            WHERE standard_word IS NULL 
            """
    return pd.read_sql_query(query, conn)


def insert_model_standard_word(standard_word: str, word: str):
    query = f"""
                UPDATE keywords_job_model 
                SET standard_word = '{standard_word}'
                WHERE keyword_name = '{word}'
             """
    conn.execute(query)
    logger.info(f"update success, {word}: {standard_word}")


def select_standard_word(other_word: str) -> str:
    if '%' in other_word:
        other_word += '%'
    query = f"""
                SELECT standard_word
                FROM standard_word 
                WHERE standard_word = '{other_word}'
             """
    res = conn.execute(query)
    if res.rowcount != 0:
        return res.fetchone()[0]
    else:
        return select_standard_word_by_other_word(other_word)


def select_standard_word_by_other_word(other_word: str) -> str:
    query = f"""
                SELECT standard_word
                FROM standard_word 
                WHERE other_words LIKE '%%,{other_word},%%'
             """
    res = conn.execute(query)
    if res.rowcount != 0:
        return res.fetchone()[0]
    else:
        return other_word


def select_standard_category(word: str) -> str:
    query = f"""
                SELECT category
                FROM standard_word 
                WHERE standard_word = '{word}'
             """
    res = conn.execute(query)
    if res.rowcount != 0:
        return res.fetchone()[0]
    else:
        return ""
