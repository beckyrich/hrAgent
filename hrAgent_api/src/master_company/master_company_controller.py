from nest.core import Controller, Get, Post, Depends

from src.master_company.master_company_service import MasterCompanyService
from src.master_company.master_company_model import MasterCompany


@Controller("master_company")
class MasterCompanyController:
    service: MasterCompanyService = Depends(MasterCompanyService)

    @Get("/")
    def get_master_company(self, with_children: bool=False, id: int=None, company_name: str = None):
        if not with_children:
            return self.service.get_master_company()
        
        # Make the query to the get_master_company 
        master_co = self.service.get_one_master_company(id=id, company_name=company_name)
        # Take the ID from the get_master_company and pass to the 
        # company.get_company with master id
        
        
        return master_co


    @Post("/add_master_company")
    def add_master_company(self, master_company: MasterCompany):
        return self.service.add_master_company(master_company)
