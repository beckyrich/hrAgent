from orm_config import config
from sqlalchemy import Column, Integer, String, Float, BigInteger, DateTime, Numeric


class PlacementHistory(config.Base):
    __tablename__ = "placement_history"

    placement_history_id = Column(BigInteger, primary_key=True, autoincrement=True)
    job_id = Column(BigInteger)
    company_id = Column(BigInteger)
    candidate_id = Column(BigInteger)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    created = Column(DateTime)
    last_updated = Column(DateTime)
    hiring_manager_id = Column(Integer)
    hourly_bill_rate = Column(Float)
    hourly_pay_rate = Column(Float)
