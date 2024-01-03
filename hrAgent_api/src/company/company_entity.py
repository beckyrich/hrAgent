from orm_config import config
from sqlalchemy import Column, Integer, String, Float, BigInteger
    
    
class Company(config.Base):
    __tablename__ = "master_company"
    
    master_company_id = Column(BigInteger, primary_key=True, autoincrement=True)
    co_name = Column(String, unique=True)
    address_line_1 = Column(String)
    address_line_2 = Column(String)
        
    