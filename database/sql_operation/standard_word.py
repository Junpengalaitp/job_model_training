from datetime import datetime

import pandas as pd

from database.sqlalchemy_manager import conn, logger


def insert_standard_words(standard_word: str, other_words: str, category: str):
    query = f"""
                INSERT INTO standard_words (standard_word, other_words, category, modification_time) VALUES (
                '{standard_word}', '{other_words}', '{category}', '{datetime.now()}')
                ON DUPLICATE KEY UPDATE other_words = '{other_words}', modification_time = '{datetime.now()}';
             """
    conn.execute(query)
    logger.info(f"insert success, standard_word: {standard_word}, other_words: {other_words}")


def update_stand_words(standard_word, other_words):
    query = f"""
                UPDATE standard_words 
                SET other_words = '{other_words}', modification_time = '{datetime.now()}' 
                WHERE standard_word = '{standard_word}'
             """
    conn.execute(query)
    logger.info(f"update success, standard_word: {standard_word}, other_words: {other_words}")


def select_standard_words(standard_word):
    query = f"""
                SELECT * FROM standard_words WHERE standard_word = '{standard_word}'
             """
    return pd.read_sql_query(query, conn)
