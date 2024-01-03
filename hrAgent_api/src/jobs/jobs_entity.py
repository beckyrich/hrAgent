from orm_config import config
from sqlalchemy import Column, Integer, String, Float, Enum, Boolean
    
    
class Jobs(config.Base):
    __tablename__ = "jobs"
    
    job_id = Column(BigInteger, primary_key=True, autoincrement=True)
    job_type = Column(Enum)
    job_title = Column(String)
    job_level = Column(Enum)
    remote = Column(Boolean)
    created = Column(TimeStamp)
    last_updated = Column(TimeStamp)
        
    