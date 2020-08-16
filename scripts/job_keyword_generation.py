import logging
import os
import sys
from concurrent.futures.process import ProcessPoolExecutor

import spacy
from loguru import logger

from concurrency.CountDownLatch import CountDownLatch
from concurrency.JobKeywordGenerationProcess import JobKeywordGenerationProcess
from concurrency.JobKeywordGenerationThread import JobKeywordGenerationThread
from database.sql_operation.standard_word import select_all_dice_jobs
from util.timer import timeit

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
model_path = os.path.join(BASE_DIR, "job_model_sm")
sys.path.append(model_path)

nlp = spacy.load('job_model_sm')


@timeit
def run():
    jobs_df = select_all_dice_jobs()
    jobs_amount = len(jobs_df)
    logging.info(f"retrieved {jobs_amount} jobs")
    threads = [JobKeywordGenerationProcess(job_df, nlp) for job_df in jobs_df.itertuples()]
    count_down_latch = CountDownLatch(len(threads))
    with ProcessPoolExecutor(max_workers=os.cpu_count() * 4) as executor:
        for thread in threads:
            try:
                executor.submit(thread.run(count_down_latch))
            except:
                continue
    logger.info("all job keywords persisted")


if __name__ == '__main__':
    run()
