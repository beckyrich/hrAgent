from datetime import datetime
from pydantic import BaseModel
    
    
class Company(BaseModel):
    company_id: int
    parent_co_id: int
    address_line1: str
    address_line2: str
    postal_code: str
    state_id: int
    created: datetime
    last_updated: datetime
    point_of_contact: str
    poc_email: str
