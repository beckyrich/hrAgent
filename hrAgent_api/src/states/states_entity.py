from orm_config import config
from sqlalchemy import Column, Integer, String, Float, DateTime, SmallInteger


class States(config.Base):
    __tablename__ = "states"

    state_id = Column(SmallInteger, primary_key=True, autoincrement=True)
    state_abbv = Column(String)
    state_name = Column(String, nullable=False)
    state_capital = Column(String)
    created = Column(DateTime)
    last_updated = Column(DateTime)
