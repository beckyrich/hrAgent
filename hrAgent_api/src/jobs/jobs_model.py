from src.jobs.jobs_enums import JobTypeEnum, JobLevelEnum
from datetime import datetime
from pydantic import BaseModel


class Jobs(BaseModel):
    company_id: int
    job_type: JobTypeEnum = JobTypeEnum.seasonal
    job_title: str
    jobs_level: JobLevelEnum = JobLevelEnum.entry
    remote: bool
    created: datetime
    last_updated: datetime
