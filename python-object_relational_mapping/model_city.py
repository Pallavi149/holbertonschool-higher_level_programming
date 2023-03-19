#!/usr/bin/python3
"""
Module containing the class definition of city
and an instance Base = declarative_base()
"""


from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Creating the City class as a child of Base"""
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")


State.cities = relationship("City",
                            order_by=City.id, back_populates="state")
