from datetime import datetime
from pydantic import BaseModel


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
