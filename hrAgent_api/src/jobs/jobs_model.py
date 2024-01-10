from datetime import datetime
from enum import Enum
from pydantic import BaseModel

class JobTypeEnum(str, Enum):
    seasonal = 'seasonal'
    fte = 'fte'
    part_time = 'part_time'
    ten_99 = 'ten_99'
    agency = 'agency'
    contract_to_hire = 'contract_to_hire'

class JobLevelEnum(str, Enum):
    entry = 'entry'
    mid = 'mid'
    senior = 'senior'
    principal = 'principal'
    management = 'management'
    executive = 'executive'
    
class Jobs(BaseModel):
    job_id: str
    job_type: JobTypeEnum = JobTypeEnum.seasonal
    job_title: str
    jobs_level: JobLevelEnum = JobLevelEnum.entry
    remote: bool
    created: datetime = None
    last_updated: datetime = None
