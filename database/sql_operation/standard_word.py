from datetime import datetime

import pandas as pd
import sqlalchemy

from database.sqlalchemy_manager import conn, logger


def insert_standard_words(standard_word: str, other_words: str, category: str):
    query = f"""
                INSERT INTO standard_words (standard_word, other_words, category, modification_time) VALUES (
                "{standard_word}", "{other_words}", "{category}", "{datetime.now()}")
                ON DUPLICATE KEY UPDATE other_words = "{other_words}", modification_time = "{datetime.now()}";
             """
    conn.execute(query)
    logger.info(f"insert success, standard_word: {standard_word}, other_words: {other_words}")


def update_stand_words(standard_word, other_words, category):
    query = f"""
                UPDATE standard_words 
                SET other_words = "{other_words}", modification_time = "{datetime.now()}" , category = "{category}"
                WHERE standard_word = "{standard_word}"
             """
    conn.execute(query)
    logger.info(f"update success, standard_word: {standard_word}, other_words: {other_words}")


def delete_stand_word(standard_word):
    query = f"""
                    DELETE FROM standard_words 
                    WHERE standard_word = "{standard_word}"
                 """
    conn.execute(query)
    logger.info(f"delete success, standard_word: {standard_word}")


def select_standard_words(standard_word):
    query = f"""
                SELECT * FROM standard_words WHERE standard_word = "{standard_word}"
             """
    return pd.read_sql_query(query, conn)


def select_all_standard_words():
    query = f"""
                SELECT * FROM standard_words
             """
    return pd.read_sql_query(query, conn)


def select_job_by_id(_job_id):
    query = f"""
                SELECT * FROM dice_jobs where job_id = '{_job_id}'
             """
    return pd.read_sql_query(query, conn)


def insert_job(job: dict):
    df = pd.DataFrame([job])
    df.to_sql("dice_jobs", if_exists='append', index=False, con=conn, dtype={
        'job_id': sqlalchemy.types.VARCHAR(length=255),
        'title': sqlalchemy.types.VARCHAR(length=255),
        'company': sqlalchemy.types.VARCHAR(length=255),
        'location': sqlalchemy.types.VARCHAR(length=255),
        'tags': sqlalchemy.types.VARCHAR(length=255),
        'category': sqlalchemy.types.VARCHAR(length=255),
        'job_desc': sqlalchemy.types.TEXT(),
        'raw_desc': sqlalchemy.types.TEXT(),
        'link': sqlalchemy.types.VARCHAR(length=255),
        'source': sqlalchemy.types.VARCHAR(length=255),
        'state': sqlalchemy.types.VARCHAR(length=255),
        'salary': sqlalchemy.types.VARCHAR(length=255),
        'employment_type': sqlalchemy.types.VARCHAR(length=255),
        'remote_available': sqlalchemy.types.VARCHAR(length=255),
        'job_date': sqlalchemy.types.VARCHAR(length=255),
        'crawled_time': sqlalchemy.types.DateTime(),

    })
    logger.info(f"insert success, id: {job['job_id']}")