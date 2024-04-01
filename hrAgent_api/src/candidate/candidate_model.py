from datetime import datetime, UTC
from pydantic import BaseModel
from typing import Optional


class Candidate(BaseModel):
    candidate_id: int
    candidate_first_name: str
    candidate_last_name: str
    candidate_email: str
    candidate_phone: int
    candidate_birthdate: datetime
    candidate_gender_id: int
    created: datetime
    last_updated: datetime
    last_login: datetime
    status_id: int


class Application(BaseModel):
    job_id: str
    candidate_id: int


class ApplicationUpdate(Application):
    status: Optional[int]
    last_updated: datetime = datetime.now(UTC)
