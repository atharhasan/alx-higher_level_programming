#!/usr/bin/python3
''' the class definition of a City and an instance Base '''


from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    ''' Define a City with id and name '''
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,  ForeignKey('states.id'), nullable=False)
