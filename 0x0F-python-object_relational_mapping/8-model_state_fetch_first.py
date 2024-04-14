#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    script that connects to a database using sqlalchemy and retrieves the first
    record of a table based on id field
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
    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    engine.dispose()
