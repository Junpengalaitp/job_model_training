from database.MysqlManager import MysqlManager


def insert_job_keywords(**kwargs):
    query = f"""
            INSERT INTO job_keywords (keyword_name, job_id, created_time, count, source, keyword_type)
            VALUES ('{kwargs['keyword_name']}', '{kwargs['job_id']}', '{kwargs['created_time']}', '{kwargs['count']}',
                    '{kwargs['source']}', '{kwargs['keyword_type']}')
            """
    MysqlManager(1).insert(query)


def insert_job_keywords_raw(**kwargs):
    query = f"""
            INSERT INTO github_keywords_raw (keyword_name, job_id, created_time, count, source, keyword_type)
            VALUES ('{kwargs['keyword_name']}', '{kwargs['job_id']}', '{kwargs['created_time']}', '{kwargs['count']}',
                    '{kwargs['source']}', '{kwargs['keyword_type']}')
            """
    MysqlManager(1).insert(query)


def insert_job_experience_raw(**kwargs):
    query = f"""
            INSERT INTO github_experience_raw (keyword_name, job_id, created_time, count, source, keyword_type)
            VALUES ('{str(kwargs['keyword_name'])}', '{kwargs['job_id']}', '{kwargs['created_time']}', '{kwargs['count']}',
                    '{kwargs['source']}', '{kwargs['keyword_type']}')
            """
    MysqlManager(1).insert(query)



