from src.candidate.candidate_model import Candidate
from src.candidate.candidate_entity import Candidate as CandidateEntity
from orm_config import config
from nest.core.decorators import db_request_handler
from functools import lru_cache


@lru_cache()
class CandidateService:
    def __init__(self):
        self.orm_config = config
        self.session = self.orm_config.get_db()

    @db_request_handler
    def add_candidate(self, candidate: Candidate):
        new_candidate = CandidateEntity(**candidate.dict())
        self.session.add(new_candidate)
        self.session.commit()
        return new_candidate.candidate_id

    @db_request_handler
    def get_candidate(self):
        return self.session.query(CandidateEntity).all()
