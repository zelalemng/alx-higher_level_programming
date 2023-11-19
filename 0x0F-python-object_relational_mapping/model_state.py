#!/usr/bin/python3
"""contains the class definition of a State and an instance Base
= declarativw_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class State(Base):
    """inherits from base, link to mysql table states"""
    __tablename__ = 'states'
    id = Column(
            Integer,
            unique=True,
            nullable=False,
            autoincrement=True,
            primary_key+True)
    name = Column(String(128), nullable=False)
