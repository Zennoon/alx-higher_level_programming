#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    script that retrieves cities by states
"""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    args = sys.argv
    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(args[1], args[2], args[3]))
    session = sessionmaker(bind=engine)()
    s_and_cs = session.query(State, City).filter(State.id == City.state_id)
    s_and_cs = s_and_cs.order_by(City.id).all()
    for state, city in s_and_cs:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
