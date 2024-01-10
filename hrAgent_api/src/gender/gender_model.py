from datetime import datetime
from pydantic import BaseModel
    
    
class Gender(BaseModel):
    gender_id: int
    gender_desc: str
    created: datetime
    last_updated: datetime
    