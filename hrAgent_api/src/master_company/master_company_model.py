from datetime import datetime
from pydantic import BaseModel
from typing import Optional
    
    
class MasterCompany(BaseModel):
    master_company_id: Optional[int] = None
    co_name: str
    address_line_1: str
    address_line_2: Optional[str] = None
    postal_code: str
    state_id: int
    company_type: int
    status_id: int
