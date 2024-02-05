from src.company.company_model import Company
from src.company.company_entity import Company as CompanyEntity
from orm_config import config
from nest.core.decorators import db_request_handler
from functools import lru_cache
from sqlalchemy import select


@lru_cache()
class CompanyService:
    def __init__(self):
        self.orm_config = config
        self.session = self.orm_config.get_db()

    @db_request_handler
    def add_company(self, company: Company):
        new_company = CompanyEntity(**company.dict())
        self.session.add(new_company)
        self.session.commit()
        return new_company.company_id

    @db_request_handler
    def get_company(self, master_co_id: int = None):
        if master_co_id is None:
            return self.session.query(CompanyEntity).all()
        return self.session.scalars(
            select(CompanyEntity).where(CompanyEntity.parent_co_id == master_co_id)
        ).all()
