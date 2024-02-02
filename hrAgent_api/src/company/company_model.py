from datetime import datetime
from pydantic import BaseModel
from typing import Optional
    
    
class Company(BaseModel):
    parent_co_id: int
    address_line_1: str
    address_line_2: Optional[str] = None
    postal_code: str
    state_id: int
    created: datetime
    last_updated: datetime
    point_of_contact: str
    poc_email: str
