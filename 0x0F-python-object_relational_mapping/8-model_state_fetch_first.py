#!/usr/bin/python3
"""
a script that prints the first State object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State).filter_by(id='1'):
        if row.id == 1:
            print("{}: {}".format(row.id, row.name))
        else:
            print("Nothing")
