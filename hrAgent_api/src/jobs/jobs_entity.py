import enum
from orm_config import config
from sqlalchemy import Column, Integer, String, Float, Enum, Boolean, DateTime, BigInteger
    
class JobType(enum.Enum):
    seasonal = 1
    fte = 2
    part_time = 3
    ten_99 = 4
    agency = 5
    contract_to_hire = 6

class JobLevel(enum.Enum):
    entry = 1
    mid = 2
    senior = 3
    principal = 4
    management = 5
    executive = 6    

class Jobs(config.Base):
    __tablename__ = "jobs"
    
    job_id = Column(BigInteger, primary_key=True, autoincrement=True)
    job_type = Column(Enum(JobType))
    job_title = Column(String)
    job_level = Column(Enum(JobLevel))
    remote = Column(Boolean)
    created = Column(DateTime)
    last_updated = Column(DateTime)
        
    