from orm_config import config
from sqlalchemy import Column, String, Float, DateTime, SmallInteger


class Gender(config.Base):
    __tablename__ = "gender"

    gender_id = Column(SmallInteger, primary_key=True)
    gender_desc = Column(String)
    created = Column(DateTime)
    last_updated = Column(DateTime)
