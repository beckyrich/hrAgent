from src.gender.gender_model import Gender
from src.gender.gender_entity import Gender as GenderEntity
from orm_config import config
from nest.core.decorators import db_request_handler
from functools import lru_cache


@lru_cache()
class GenderService:
    def __init__(self):
        self.orm_config = config
        self.session = self.orm_config.get_db()

    @db_request_handler
    def add_gender(self, gender: Gender):
        new_gender = GenderEntity(**gender.dict())
        self.session.add(new_gender)
        self.session.commit()
        return new_gender.id

    @db_request_handler
    def get_gender(self):
        return self.session.query(GenderEntity).all()
