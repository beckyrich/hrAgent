from datetime import datetime
from pydantic import BaseModel
    
    
class Jobs(BaseModel):
    job_id: str
    job_type:
    job_title: str
    jobs_level: 
    remote: bool
    created: datetime
    last_updated: datetime
    