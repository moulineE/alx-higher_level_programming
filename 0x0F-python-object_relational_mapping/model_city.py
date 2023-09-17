#!/usr/bin/python3
"""
python file that contains the class definition of a City and
an instance Base = declarative_base()
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    class definition of a City that inherits from Base

    Attributes:
        id (int): column of an auto-generated, unique integer, pKey
        name (str): column of a string with maximum 128 characters
        state_id (int)  column of an auto-gen, unique integer,fKey=states.id

    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
