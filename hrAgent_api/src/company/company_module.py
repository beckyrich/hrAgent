from src.company.company_service import CompanyService
from src.company.company_controller import CompanyController


class CompanyModule:
    def __init__(self):
        self.providers = [CompanyService]
        self.controllers = [CompanyController]
