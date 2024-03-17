#!/usr/bin/python3
"""model city"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """City class that inharite from Base"""

    __tablename__ = "cities"
    id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False, unique=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
