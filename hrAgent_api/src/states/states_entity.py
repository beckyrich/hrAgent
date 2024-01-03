from orm_config import config
from sqlalchemy import Column, Integer, String, Float, TimeStamp, SmallInteger
    
    
class States(config.Base):
    __tablename__ = "states"
    
    state_id = Column(SmallInteger, primary_key=True, autoincrement=True)
    state_abbv = Column(String)
    state_name = Column(String)
    state_capital = Column(String)
    created = Column(TimeStamp)
    last_updated = Column(TimeStamp)
        
    