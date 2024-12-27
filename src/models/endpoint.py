from src.models.base import Base, TimestampMixin
from sqlalchemy import Column, Integer, String, Interval, ForeignKey
from sqlalchemy.orm import relationship


class Endpoint(Base, TimestampMixin):
    __tablename__ = "endpoints"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    method = Column(String, nullable=False, default="GET")
    headers = Column(String, nullable=False)
    check_interval = Column(Interval, nullable=False)
    expected_status_code = Column(Integer, nullable=True)
    timeout = Column(Integer, default=30)
    retry_count = Column(Integer, default=3)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="endpoints")
    checks = relationship("Check", back_populates="endpoints", cascade="all, delete-orphan")