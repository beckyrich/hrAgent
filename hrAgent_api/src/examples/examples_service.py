from src.examples.examples_model import Examples
from src.examples.examples_entity import Examples as ExamplesEntity
from orm_config import config
from nest.core.decorators import db_request_handler
from functools import lru_cache


@lru_cache()
class ExamplesService:

    def __init__(self):
        self.orm_config = config
        self.session = self.orm_config.get_db()
    
    @db_request_handler
    def add_examples(self, examples: Examples):
        new_examples = ExamplesEntity(
            **examples.dict()
        )
        self.session.add(new_examples)
        self.session.commit()
        return new_examples.id

    @db_request_handler
    def get_examples(self):
        return self.session.query(ExamplesEntity).all()
 