#!/usr/bin/python3
"""this module contains a script to list all states using module SQLAlchemy"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
from sqlalchemy import create_engine


if __name__ == '__main__':
    myengine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                             .format(sys.argv[1], sys.argv[2], sys.argv[3],
                                     pool_pre_ping=True))
    Base.metadata.create_all(myengine)
    Session = sessionmaker(bind=myengine)
    session = Session()
    for record in session.query(State).order_by(State.id):
        print("{}: {}".format(record.id, record.name))
