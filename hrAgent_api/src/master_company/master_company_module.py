from src.master_company.master_company_service import MasterCompanyService
from src.master_company.master_company_controller import MasterCompanyController


class MasterCompanyModule:

    def __init__(self):
        self.providers = [MasterCompanyService]
        self.controllers = [MasterCompanyController]



