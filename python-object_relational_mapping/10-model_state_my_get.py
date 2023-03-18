#!/usr/bin/python3
"""prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    name = sys.argv[4]
    query = session.query(State)\
                   .filter(State.name == name).order_by(State.id)
    try:
        state = query.one()
        print("{}".format(state.id))
    except NoResultFound:
        sys.stderr.write("Not Found\n")
