from src.models.base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship


class Check(Base):
    __tablename__ = "checks"

    id = Column(Integer, primary_key=True, index=True)
    endpoint_id = Column(Integer, ForeignKey("endpoints"), nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False)
    response_time = Column(Float)
    error_message = Column(String, nullable=True)
    is_successful = Column(Boolean)
    response_size = Column(Integer, nullable=True)

    endpoint = relationship("Endpoint", back_populates="checks")