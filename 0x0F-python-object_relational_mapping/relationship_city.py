#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Classes
    =======
    City - Inherits from Base and maps to 'cities' table of a database
"""
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """Inherits from declarative_base() and maps to a table of a database."""
    __tablename__ = "cities"
    id = Column(Integer, autoincrement="auto", primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
    state = relationship("State", back_populates="cities")


State.cities = relationship("City", back_populates="state",
                            cascade="all, delete, delete-orphan")
