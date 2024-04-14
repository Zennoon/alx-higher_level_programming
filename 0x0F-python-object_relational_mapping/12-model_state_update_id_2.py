#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    script that retrieves a record with known id and alters/updates its name
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

    state = session.query(State).filter(State.id == 2).one_or_none()
    if state:
        state.name = "New Mexico"
    session.commit()
    engine.dispose()
