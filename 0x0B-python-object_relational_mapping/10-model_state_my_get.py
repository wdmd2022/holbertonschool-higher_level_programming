#!/usr/bin/python3
"""this module contains a script to print the State object with the name
passed as arg from the database hbtn_0e_6_usa using module SQLAlchemy"""

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
    record = session.query(State).filter_by(name=sys.argv[4]).first()
    if record:
        print("{}".format(record.id))
    else:
        print("Not found")
