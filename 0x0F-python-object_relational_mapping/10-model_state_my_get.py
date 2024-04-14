#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    script that retrieves a record of a table whose 'name' field's value equals
    a string given as a command line argument
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    args = sys.argv
    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(args[1], args[2], args[3]))
    session = sessionmaker(bind=engine)()
    args[4] = args[4].replace("'", "")
    state_id = session.query(State.id)
    state_id = state_id.filter(State.name == args[4]).one_or_none()
    if state_id:
        print(state_id.id)
    else:
        print("Not found")
    engine.dispose()
