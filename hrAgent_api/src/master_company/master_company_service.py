from src.master_company.master_company_model import MasterCompany
from src.master_company.master_company_entity import MasterCompany as MasterCompanyEntity
from orm_config import config
from nest.core.decorators import db_request_handler
from functools import lru_cache


@lru_cache()
class MasterCompanyService:

    def __init__(self):
        self.orm_config = config
        self.session = self.orm_config.get_db()
    
    @db_request_handler
    def add_master_company(self, master_company: MasterCompany):
        new_master_company = MasterCompanyEntity(
            **master_company.dict()
        )
        self.session.add(new_master_company)
        self.session.commit()
        return new_master_company.id

    @db_request_handler
    def get_master_company(self):
        return self.session.query(MasterCompanyEntity).all()
 