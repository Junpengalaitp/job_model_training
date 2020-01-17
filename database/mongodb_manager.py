import logging
from pymongo import MongoClient

from logger.logger import setup_logging
from config import read_config

setup_logging()
logger = logging.getLogger("dbLogger")


class MongoManager:
    def __init__(self):
        mongo_ip = read_config.get_config('mongodb', 'ip')
        mongo_port = int(read_config.get_config('mongodb', 'port'))
        username = read_config.get_config('mongodb', 'username')
        password = read_config.get_config('mongodb', 'password')
        self.client = MongoClient(f'mongodb://{username}:{password}@{mongo_ip}', mongo_port)

    def find_all(self):
        db = self.client.remotive_jobs
        jobs = db.software_dev.find({})
        job_list = [job for job in jobs]
        return job_list

    def find_one_by_id(self, job_id):
        db = self.client.tech_job
        job = db.dice.find_one({'job_id': job_id}, {'_id': False})
        return job

    def find_distinct_dice_ids(self, field):
        db = self.client.tech_job
        fields = db.dice.distinct(field)
        return [f for f in fields]



