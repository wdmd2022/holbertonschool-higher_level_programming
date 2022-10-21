#!/usr/bin/python3
"""this module contains a script to print all city objects from the database
hbtn_0e_14_usa, using module SQLAlchemy."""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from model_city import City


if __name__ == '__main__':
    myengine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                             .format(sys.argv[1], sys.argv[2], sys.argv[3],
                                     pool_pre_ping=True))
    Base.metadata.create_all(myengine)
    Session = sessionmaker(bind=myengine)
    session = Session()
    for my_state, my_city_id, my_city in session.query(
        State.name, City.id, City.name).filter(City.state_id == State.id)\
            .order_by(City.id):
        print("{}: ({}) {}".format(my_state, my_city_id, my_city))
    session.close()
