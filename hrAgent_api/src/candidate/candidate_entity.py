from orm_config import config
from datetime import datetime, UTC
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    BigInteger,
    Numeric,
    Date,
    SmallInteger,
    DateTime,
)


class Candidate(config.Base):
    __tablename__ = "candidate"

    candidate_id = Column(BigInteger, primary_key=True, autoincrement=True)
    candidate_first_name = Column(String)
    candidate_last_name = Column(String)
    candidate_email = Column(String, unique=True, nullable=False)
    candidate_phone = Column(Numeric)
    candidate_birthdate = Column(Date)
    candidate_gender_id = Column(SmallInteger)
    created = Column(DateTime)
    last_updated = Column(DateTime)
    last_login = Column(DateTime)
    status_id = Column(Integer)


class Application(config.Base):
    __tablename__ = "application"

    application_id = Column(BigInteger, primary_key=True, autoincrement=True)
    job_id = Column(BigInteger, nullable=False)
    candidate_id = Column(BigInteger, nullable=False)
    status = Column(Integer, default=1)
    created = Column(DateTime, default=datetime.now(UTC))
    last_updated = Column(DateTime, default=datetime.now(UTC))
