from orm_config import config
from sqlalchemy import Column, Integer, String, Float, BigInteger, TimeStamp, Numeric
    
    
class PlacementHistory(config.Base):
    __tablename__ = "placement_history"
    
    placement_history_id = Column(BigInteger, primary_key=True, autoincrement=True)
    job_id = Column(BigInteger)
    company_id = Column(BigInteger)
    candidate_id = Column(BigInteger)
    start_date = Column(TimeStamp)
    end_date = Column(TimeStamp)
    created = Column(TimeStamp)
    last_updated = Column(TimeStamp)
    hiring_manager_id = Column(Integer)
    hourly_bill_rate = Column(Numeric)
    hourly_pay_rate = Column(Numeric)
        
    