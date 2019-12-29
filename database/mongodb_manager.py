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


