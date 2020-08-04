from pymongo import MongoClient

from config.settings import MONGO_IP, MONGO_PORT


class MongoManager:
    def __init__(self):
        mongo_ip = MONGO_IP
        mongo_port = MONGO_PORT
        self.client = MongoClient(f'mongodb://{mongo_ip}', mongo_port)

    def find_all(self):
        db = self.client.remotive_jobs
        jobs = db.software_dev.find({})
        job_list = [job for job in jobs]
        return job_list

    def find_one_by_id(self, database, job_id):
        if database == 'dice_job':
            db = self.client.tech_job
            job = db.dice.find_one({'job_id': job_id}, {'_id': False})
        if database == 'remote_job':
            db = self.client.remote_jobs
            job = db.software_dev.find_one({'job_id': job_id}, {'_id': False})
        return job

    def find_distinct_dice_field(self, field):
        db = self.client.tech_job
        fields = db.dice.distinct(field)
        return [f for f in fields]

    def find_distinct_remote_field(self, field):
        db = self.client.remote_jobs
        fields = db.software_dev.distinct(field)
        return [f for f in fields]



