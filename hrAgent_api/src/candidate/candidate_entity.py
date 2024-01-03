from orm_config import config
from sqlalchemy import Column, Integer, String, Float
    
    
class Candidate(config.Base):
    __tablename__ = "candidate"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
        
    