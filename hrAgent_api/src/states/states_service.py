from src.states.states_model import States
from src.states.states_entity import States as StatesEntity
from orm_config import config
from nest.core.decorators import db_request_handler
from functools import lru_cache
from sqlalchemy import select

@lru_cache()
class StatesService:

    def __init__(self):
        self.orm_config = config
        self.session = self.orm_config.get_db()
    
    @db_request_handler
    def add_states(self, states: States):
        new_states = StatesEntity(
            **states.dict()
        )
        self.session.add(new_states)
        self.session.commit()
        return new_states.state_id

    @db_request_handler
    def get_states(self):
        return self.session.scalars(
            select(StatesEntity)
        ).all()
    
    @db_request_handler
    def get_one_state(self, abbv: str = "FL"):
        return self.session.scalars(select(StatesEntity).where(StatesEntity.state_abbv == abbv)).all()
 