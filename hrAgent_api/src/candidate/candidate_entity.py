from orm_config import config
from sqlalchemy import Column, Integer, String, Float, BigInteger, Numeric, Date, SmallInteger, TimeStamp
    
    
class Candidate(config.Base):
    __tablename__ = "candidate"
    
    candidate_id = Column(BigInteger, primary_key=True, autoincrement=True)
    candidate_first_name = Column(String)
    candidate_last_name = Column(String)
    candidate_email = Column(String, unique=True)
    candidate_phone = Column(Numeric)
    candidate_birthdate = Column(Date)
    candidate_gender_id = Column(SmallInteger)
    created = Column(TimeStamp)
    last_updated = Column(TimeStamp)
    last_login = Column(TimeStamp)
    status_id = Column(Integer)
        
    