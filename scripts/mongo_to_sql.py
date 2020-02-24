import traceback

from database.mongodb_manager import MongoManager
from database.sql_operation.standard_word import insert_dice_job, select_by_job_id, insert_remote_job


def get_distinct_ids(db: str) -> list:
    if db == "dice_job":
        ids = MongoManager().find_distinct_dice_field('job_id')
    if db == "remote_job":
        ids = MongoManager().find_distinct_remote_field('job_id')
    return ids


def insert_to_sql(db, job_id):
    job = MongoManager().find_one_by_id(db, job_id)
    if db == 'dice_job':
        job['salary'] = ''.join(job['salary']) if job['salary'] else None
        insert_dice_job(job)
    if db == 'remote_job':
        insert_remote_job(job)


def mongo_to_sql(db):
    ids = get_distinct_ids(db)
    for job_id in ids:
        try:
            record = select_by_job_id(db, job_id)
            if len(record) != 0:
                continue
            insert_to_sql(db, job_id)
        except:
            print(traceback.format_exc())
            continue


if __name__ == '__main__':
    mongo_to_sql('dice_job')
