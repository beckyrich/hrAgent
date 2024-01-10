import enum
from orm_config import config
from sqlalchemy import Column, Integer, String, Float, Enum, Boolean, DateTime, BigInteger
    
class JobType(enum.Enum):
    seasonal = 'seasonal'
    fte = 'fte'
    part_time = 'part_time'
    ten_99 = 'ten_99'
    agency = 'agency'
    contract_to_hire = 'contract_to_hire'

class JobLevel(enum.Enum):
    entry = 'entry'
    mid = 'mid'
    senior = 'senior'
    principal = 'principal'
    management = 'managment'
    executive = 'executive'    

class Jobs(config.Base):
    __tablename__ = "jobs"
    
    job_id = Column(BigInteger, primary_key=True, autoincrement=True)
    job_type = Column(Enum(JobType))
    job_title = Column(String)
    job_level = Column(Enum(JobLevel))
    remote = Column(Boolean)
    created = Column(DateTime)
    last_updated = Column(DateTime)
        
    