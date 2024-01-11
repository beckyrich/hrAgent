from src.jobs.jobs_enums import JobTypeEnum, JobLevelEnum
from orm_config import config
from sqlalchemy import Column, Integer, String, Float, Enum, Boolean, DateTime, BigInteger   

class Jobs(config.Base):
    __tablename__ = "jobs"
    
    job_id = Column(BigInteger, primary_key=True, autoincrement=True)
    job_type = Column(Enum(JobTypeEnum))
    job_title = Column(String)
    job_level = Column(Enum(JobLevelEnum))
    remote = Column(Boolean)
    created = Column(DateTime)
    last_updated = Column(DateTime)
        
    