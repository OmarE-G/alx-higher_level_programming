#!/usr/bin/python3
"""Base City Class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """city Class definition"""
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id',
                      ForeignKey('State.id'), Integer, nullable=False)

