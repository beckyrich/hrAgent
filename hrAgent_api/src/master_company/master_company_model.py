from datetime import datetime
from pydantic import BaseModel
    
    
class MasterCompany(BaseModel):
    master_company_id: int
    co_name: str
    address_line_1: str
    address_line_2: str
    postal_code: float
    state_id: int
    created: datetime
    last_updated: datetime
    company_type: int
    status_id: int
