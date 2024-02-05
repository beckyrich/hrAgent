from orm_config import config
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    BigInteger,
    DateTime,
    SmallInteger,
)
import datetime


class MasterCompany(config.Base):
    __tablename__ = "master_company"

    master_company_id = Column(BigInteger, primary_key=True, autoincrement=True)
    co_name = Column(String, unique=True, nullable=False)
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    postal_code = Column(String)
    state_id = Column(SmallInteger)
    created = Column(DateTime, default=datetime.datetime.utcnow())
    last_updated = Column(DateTime, default=datetime.datetime.utcnow())
    company_type = Column(Integer)
    status_id = Column(Integer)
