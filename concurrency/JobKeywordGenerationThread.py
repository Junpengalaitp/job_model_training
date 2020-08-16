import traceback
from datetime import datetime
from threading import Thread

import pandas as pd
from loguru import logger

from concurrency.CountDownLatch import CountDownLatch
from database.sql_operation.standard_word import insert_model_keywords, select_standard_word, select_standard_category


class JobKeywordGenerationThread(Thread):
    def __init__(self, df_row, nlp):
        super().__init__()
        self.df_row = df_row
        self.nlp = nlp

    def run(self, count_down_latch: CountDownLatch) -> None:
        super().run()
        count_down_latch.count_down()
        self.process_job_df()
        logger.info(f" remaining works: {count_down_latch.count}")


    def process_job_df(self):
        try:
            job_keyword_df = self.generate_job_key_words()
            insert_model_keywords(job_keyword_df)
        except:
            return

    def generate_job_key_words(self):
        job_desc = self.df_row.job_desc
        doc = self.nlp(job_desc)
        result_df = pd.DataFrame(
            columns=['keyword_name', 'standard_word', 'keyword_type', 'count', "job_title", "job_id", "source",
                     "created_time"])
        result_df['keyword_name'] = [w.text for w in doc.ents if not w.text.isspace()]
        result_df['keyword_type'] = [w.label_ for w in doc.ents if not w.text.isspace()]
        result_df['count'] = [result_df['keyword_name'].values.tolist().count(e) for e in
                              result_df['keyword_name'].values.tolist()]
        result_df.drop_duplicates('keyword_name', inplace=True)
        result_df.reset_index(drop=True, inplace=True)

        for row in result_df.itertuples():
            try:
                standard_word = select_standard_word(row.keyword_name)
                result_df.at[row.Index, 'standard_word'] = standard_word
                standard_category = select_standard_category(standard_word)
                if standard_category != "" and standard_category != row.keyword_type:
                    result_df.at[row.Index, 'keyword_type'] = standard_category
                    logger.debug(f"standardized category of word: {row.keyword_name} from {row.keyword_type} to {standard_category}")
            except:
                traceback.print_exc()
                logger.error(f"error word: {row.keyword_name}")
                continue

        result_df['job_title'] = self.df_row.title
        result_df['job_id'] = self.df_row.job_id
        result_df['source'] = 'dice'
        result_df['created_time'] = datetime.now()
        return result_df
