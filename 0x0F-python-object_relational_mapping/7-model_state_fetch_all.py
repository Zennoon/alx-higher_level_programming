#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    script that connects to a database using SQLAlchemy and retrieves all
    records of a table 'states'
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
    states = session.query(State.name).order_by(State.id).all()
    for idx, state in enumerate(states):
        print("{}: {}".format(idx + 1, state.name))
    engine.dispose()
