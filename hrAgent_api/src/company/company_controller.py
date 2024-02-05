from nest.core import Controller, Get, Post, Depends

from src.company.company_service import CompanyService
from src.company.company_model import Company


@Controller("company")
class CompanyController:
    service: CompanyService = Depends(CompanyService)

    @Get("/")
    def get_company(self):
        return self.service.get_company()

    @Get("/by-parent")
    def get_company_by_parent(self, master_co_id: int):
        return self.service.get_company(master_co_id=master_co_id)

    @Post("/")
    def add_company(self, company: Company):
        return self.service.add_company(company)
