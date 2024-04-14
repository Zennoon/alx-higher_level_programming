#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Script that creates a new state
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    args = sys.argv
    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(args[1], args[2], args[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    new_state = State(name="California")
    print(new_state)
    print(new_state.cities)
    new_state.cities = [City(name="San Francisco")]
    print(new_state.cities[0].state)
    session.add(new_state)
    session.commit()
