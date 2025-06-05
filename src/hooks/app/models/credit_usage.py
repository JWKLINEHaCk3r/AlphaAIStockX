from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.base_class import Base

class CreditUsage(Base):
    __tablename__ = "credit_usage"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    used = Column(Float, default=0.0)
    available = Column(Float, default=0.0)
    limit = Column(Float, default=0.0)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
