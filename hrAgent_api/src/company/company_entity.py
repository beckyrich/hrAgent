from orm_config import config
from sqlalchemy import Column, Integer, String, Float, BigInteger, Numeric, TimeStamp
    
    
class Company(config.Base):
    __tablename__ = "company"
    
    company_id = Column(BigInteger, primary_key=True, autoincrement=True)
    parent_co_id = Column(BigInteger)
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    postal_code = Column(Numeric)
    state_id = Column(SmallInteger)
    created = Column(TimeStamp)
    last_updated = Column(TimeStamp)
    point_of_contact = Column(String)
    poc_email = Column(String)

        
    