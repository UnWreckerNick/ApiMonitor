from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict
from datetime import datetime, timedelta

class EndpointBase(BaseModel):
    name: str
    url: HttpUrl
    method: str = "GET"
    headers: Optional[Dict[str, str]] = None
    check_interval: timedelta
    expected_status_code: Optional[int] = 200
    timeout: int = 30
    retry_count: int = 3

class EndpointCreate(EndpointBase):
    pass

class EndpointUpdate(EndpointBase):
    pass

class EndpointInDB(EndpointBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True