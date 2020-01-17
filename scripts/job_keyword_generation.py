import logging
from datetime import datetime

import pandas as pd
import spacy

from database.mongodb_manager import MongoManager
from database.MysqlOperations.job_keyword_operations import insert_job_keywords_raw, insert_job_keywords_job_model
from preprocessing.clean_text import clean_html_tags, clean_text


# nlp = spacy.load('en_core_web_lg')
from database.sql_operation.standard_word import form_job_keyword_sql_params, select_all_dice_jobs

nlp = spacy.load('job_model')
# nlp.add_pipe(LanguageDetector(), name='language_detector', last=True)


def run():
    jobs_df = select_all_dice_jobs()
    jobs_amount = len(jobs_df)
    logging.info(f"retrieved {jobs_amount} jobs from mongo")
    job_processed = 0
    for job_df in jobs_df:
        job_processed += 1
        logging.info(f'===================> processing job {job_processed}/{len(jobs_df)}')
        try:
            process_job_raw(job_df)
        except:
            job_processed += 1
            continue


def process_job_raw(job_df: pd.DataFrame):

    logging.info(f"processing job for job id : {job_df['job_id']}")
    # clean_html_tags(job)
    # clean_text(job)
    logging.info("cleaned job description")
    job_keyword_df = generate_job_key_words(job_df)
    logging.info('job keyword df generated')
    job_keyword_df.to_sql()
    # params_list = form_job_keyword_sql_params(job_df, job_keyword_df)
    logging.info('param list generated')
    # if not params_list:
    #     return
    # else:
    #     for params in params_list:
    #         insert_job_keywords_job_model(**params)


def generate_job_key_words(job_df):
    job_desc = job_df['job_desc']
    doc = nlp(job_desc)
    # language = doc._.language['language']
    # logging.info(f"this job description language is {language}")
    # if language != 'en':
    #     logging.info("this job description is not English, stop processing")
    #     return None

    result_df = pd.DataFrame(columns=['keyword_name', 'keyword_type', 'count', "job_title", "job_id", "source", "created_time"])
    result_df['keyword_name'] = [w.text for w in doc.ents if not w.text.isspace()]
    result_df['keyword_type'] = [w.label_ for w in doc.ents if not w.text.isspace()]
    result_df['count'] = [result_df['keyword_name'].values.tolist().count(e) for e in result_df['keyword_name'].values.tolist()]
    result_df.drop_duplicates('keyword', inplace=True)
    result_df.reset_index(drop=True, inplace=True)

    result_df['job_title'] = job_df['job_title']
    result_df['job_id'] = job_df['job_id']
    result_df['source'] = 'dice'
    result_df['created_time'] = datetime.now()

    return result_df


if __name__ == '__main__':
    run()
