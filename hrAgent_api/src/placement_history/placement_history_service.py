from src.placement_history.placement_history_model import PlacementHistory
from src.placement_history.placement_history_entity import (
    PlacementHistory as PlacementHistoryEntity,
)
from orm_config import config
from nest.core.decorators import db_request_handler
from functools import lru_cache


@lru_cache()
class PlacementHistoryService:
    def __init__(self):
        self.orm_config = config
        self.session = self.orm_config.get_db()

    @db_request_handler
    def add_placement_history(self, placement_history: PlacementHistory):
        new_placement_history = PlacementHistoryEntity(**placement_history.dict())
        self.session.add(new_placement_history)
        self.session.commit()
        return new_placement_history.id

    @db_request_handler
    def get_placement_history(self):
        return self.session.query(PlacementHistoryEntity).all()
