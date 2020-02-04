import logging
import os
import sys
import traceback
from datetime import datetime

import pandas as pd
import spacy

# nlp = spacy.load('en_core_web_lg')
from database.sql_operation.standard_word import select_all_dice_jobs, \
    insert_model_keywords
from scripts.standardize_model_keyword import request_standard_word

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
model_path = os.path.join(BASE_DIR, "job_model_sm")
sys.path.append(model_path)

nlp = spacy.load('job_model_sm')
# nlp.add_pipe(LanguageDetector(), name='language_detector', last=True)


def run():
    jobs_df = select_all_dice_jobs()
    jobs_amount = len(jobs_df)
    logging.info(f"retrieved {jobs_amount} jobs")
    job_processed = 0
    for job_df in jobs_df.itertuples():
        job_processed += 1
        logging.info(f'===================> processing job {job_processed}/{len(jobs_df)}')
        try:
            process_job_df(job_df)
        except:
            print(traceback.format_exc())
            job_processed += 1
            continue


def process_job_df(job_df: pd.DataFrame):
    logging.info(f"processing job for job df : {job_df}")
    # clean_html_tags(job)
    # clean_text(job)
    logging.info("cleaned job description")
    job_keyword_df = generate_job_key_words(job_df)
    logging.info('job keyword df generated')
    insert_model_keywords(job_keyword_df)
    logging.info('param list generated')


def generate_job_key_words(job_df):
    job_desc = job_df.job_desc
    doc = nlp(job_desc)
    # language = doc._.language['language']
    # logging.info(f"this job description language is {language}")
    # if language != 'en':
    #     logging.info("this job description is not English, stop processing")
    #     return None

    result_df = pd.DataFrame(columns=['keyword_name', 'standard_word', 'keyword_type', 'count', "job_title", "job_id", "source", "created_time"])
    result_df['keyword_name'] = [w.text for w in doc.ents if not w.text.isspace()]
    result_df['keyword_type'] = [w.label_ for w in doc.ents if not w.text.isspace()]
    result_df['count'] = [result_df['keyword_name'].values.tolist().count(e) for e in result_df['keyword_name'].values.tolist()]
    result_df.drop_duplicates('keyword_name', inplace=True)
    result_df.reset_index(drop=True, inplace=True)

    for row in result_df.itertuples():
        standard_word = request_standard_word(row.keyword_name)
        result_df.at[row.Index, 'standard_word'] = standard_word

    result_df['job_title'] = job_df.title
    result_df['job_id'] = job_df.job_id
    result_df['source'] = 'dice'
    result_df['created_time'] = datetime.now()

    return result_df


if __name__ == '__main__':
    run()
