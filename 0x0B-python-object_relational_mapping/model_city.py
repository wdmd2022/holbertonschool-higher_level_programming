#!/usr/bin/python3
"""this module contains a class definition of a City, which as a class
inherits from Base (imported from model_state) and links to the MySQL table
`cities`. It has a class attribute `id` that representes a column of an auto-
generated, unique integer that can't be null and is a primary key. It also
has a class attribute `name` that represents a column of a string of 128 char
and can't be null. Finally, it has a class attribute `state_id` which repres-
ents a column of an integer (can't be null, and is a foreign key to states.id.
Created using the module SQLAlchemy."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """this class represents a city"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
