from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CheckBase(BaseModel):
    endpoint_id: int
    timestamp: datetime
    response_time: float
    status_code: int
    error_message: Optional[str] = None
    is_successful: bool
    response_time: Optional[int] = None

class CheckCreate(CheckBase):
    pass

class CheckInDB(CheckBase):
    id: int

    class Config:
        from_attributes = True