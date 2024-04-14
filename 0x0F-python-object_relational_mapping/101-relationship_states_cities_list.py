#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Script that uses the relationship established between classes
"""
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    args = sys.argv
    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(args[1], args[2], args[3]))
    session = sessionmaker(bind=engine)()
    all_states = session.query(State).order_by(State.id).all()
    for st in all_states:
        print("{}: {}".format(st.id, st.name))
        for c in st.cities:
            print("\t{}: {}".format(c.id, c.name))
    engine.dispose()
