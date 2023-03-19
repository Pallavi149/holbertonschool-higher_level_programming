#!/usr/bin/python3
"""
Module containing the class definition of city
and an instance Base = declarative_base()
"""


from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """Creating the City class as a child of Base"""
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship(State, backref="cities")
