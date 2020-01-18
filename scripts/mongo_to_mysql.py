from database.mongodb_manager import MongoManager
from database.sql_operation.standard_word import insert_job, select_job_by_id


def get_distinct_ids() -> list:
    ids = MongoManager().find_distinct_dice_ids('job_id')
    return ids


def insert_mysql(job_id):
    job = MongoManager().find_one_by_id(job_id)
    job['salary'] = ''.join(job['salary']) if job['salary'] else None
    insert_job(job)


if __name__ == '__main__':
    ids = get_distinct_ids()
    # for job_id in ids:
    #     try:
    #         record = select_job_by_id(job_id)
    #         if len(record) != 0:
    #             continue
    #         insert_mysql(job_id)
    #     except:
    #         continue
    print(len(ids))
