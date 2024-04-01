from src.candidate.candidate_model import Application
from src.candidate.candidate_entity import Application as ApplicationEntity
from orm_config import config
from nest.core.decorators import db_request_handler
from functools import lru_cache


@lru_cache()
class ApplicationService:
    def __init__(self):
        self.orm_config = config
        self.session = self.orm_config.get_db()

    @db_request_handler
    def get_all_applications(self):
        return self.session.query(ApplicationEntity).all()
    
    @db_request_handler
    def create_an_app(self, application: Application):
        new_app = ApplicationEntity(**application.dict())
        self.session.add(new_app)
        self.session.commit()
        return new_app.application_id
    