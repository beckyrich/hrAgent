from datetime import datetime
from pydantic import BaseModel
    
    
class States(BaseModel):
    state_id: int
    state_abbv: str
    state_name: str
    state_capital: str
    created: datetime
    last_updated: datetime
