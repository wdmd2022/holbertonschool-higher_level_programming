#!/usr/bin/python3
"""this module contains a script to add the State object `Louisiana` to
the database hbtn_0e_6_usa using module SQLAlchemy"""

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
    session.add(State(name="Louisiana"))
    added = session.query(State).filter(State.name == 'Louisiana').first()
    print("{}".format(str(added.id)))
    session.commit()
    session.close()
