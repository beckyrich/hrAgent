from nest.core import Controller, Get, Post, Depends

from src.master_company.master_company_service import MasterCompanyService
from src.master_company.master_company_model import MasterCompany


@Controller("master_company")
class MasterCompanyController:

    service: MasterCompanyService = Depends(MasterCompanyService)
    
    @Get("/get_master_company")
    def get_master_company(self):
        return self.service.get_master_company()
                
    @Post("/add_master_company")
    def add_master_company(self, master_company: MasterCompany):
        return self.service.add_master_company(master_company)
 