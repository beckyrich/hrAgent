from src.jobs.jobs_model import Jobs
from src.jobs.jobs_entity import Jobs as JobsEntity
from orm_config import config
from nest.core.decorators import db_request_handler
from functools import lru_cache


@lru_cache()
class JobsService:
    def __init__(self):
        self.orm_config = config
        self.session = self.orm_config.get_db()

    @db_request_handler
    def add_jobs(self, jobs: Jobs):
        new_jobs = JobsEntity(**jobs.dict())
        self.session.add(new_jobs)
        self.session.commit()
        return new_jobs.id

    @db_request_handler
    def get_jobs(self):
        return self.session.query(JobsEntity).all()
