from datetime import datetime
from pydantic import BaseModel
    
    
class PlacementHistory(BaseModel):
    placement_history_id: int
    job_id: int
    company_id: int
    candidate_id: int
    start_date: datetime
    end_date: datetime
    created: datetime
    last_updated: datetime
    hiring_manager_id: int
    hourly_bill_rate: float
    hourly_pay_rate: float
