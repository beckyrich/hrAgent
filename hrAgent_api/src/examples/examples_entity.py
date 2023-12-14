from orm_config import config
from sqlalchemy import Column, Integer, String, Float
    
    
class Examples(config.Base):
    __tablename__ = "examples"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
        
    