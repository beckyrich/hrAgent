from src.company.company_model import Company
from src.company.company_entity import Company as CompanyEntity
from orm_config import config
from nest.core.decorators import db_request_handler
from functools import lru_cache


@lru_cache()
class CompanyService:

    def __init__(self):
        self.orm_config = config
        self.session = self.orm_config.get_db()
    
    @db_request_handler
    def add_company(self, company: Company):
        new_company = CompanyEntity(
            **company.dict()
        )
        self.session.add(new_company)
        self.session.commit()
        return new_company.id

    @db_request_handler
    def get_company(self):
        return self.session.query(CompanyEntity).all()
 