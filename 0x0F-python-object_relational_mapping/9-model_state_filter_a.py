#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    script that retrieves the records of a table that contiain 'a' from a given
    database
"""
import sqlalchemy
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    args = sys.argv
    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(args[1], args[2], args[3]))
    session = sessionmaker(bind=engine)()
    states = session.query(State).filter(State.name.like("%a%"))
    states = states.order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    engine.dispose()
