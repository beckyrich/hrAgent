from nest.core import Controller, Get, Post, Depends

from src.company.company_service import CompanyService
from src.company.company_model import Company


@Controller("company")
class CompanyController:

    service: CompanyService = Depends(CompanyService)
    
    @Get("/")
    def get_company(self):
        return self.service.get_company()
                
    @Post("/add")
    def add_company(self, company: Company):
        return self.service.add_company(company)
 