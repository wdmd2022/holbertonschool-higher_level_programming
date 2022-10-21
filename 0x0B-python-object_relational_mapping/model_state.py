#!/usr/bin/python3
"""this module contains the class definition of a State and an instance
Base = declarative_base(). State inherits from Base, links to the MySQL
table `states`, has a class attribute id that represents a column of an
auto-generated, unique integer that can't be null and is a primary key.
It also has a class attribute name that represents a column of a string
with maximum 128 characters and can't be null. Using module SQLAlchemy"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """this class represents a State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
