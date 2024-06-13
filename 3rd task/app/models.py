from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
