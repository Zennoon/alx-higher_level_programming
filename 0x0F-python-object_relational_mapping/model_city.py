#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Classes
    =======
    City - Inherits from Base and maps to 'cities' table of a database
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Inherits from declarative_base() and maps to a table of a database."""
    __tablename__ = "cities"
    id = Column(Integer, autoincrement="auto", primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
