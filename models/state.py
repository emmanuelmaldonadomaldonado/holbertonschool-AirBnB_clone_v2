#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

if getenv('HBNB_TYPE_STORAGE') == 'db':
    cities = relationship('City', backref='State', cascade='all, delete')
else:
    
    @property
    def cities(self):
        """
        Getter for cities related to a state using a FIlEStorage engine
        """
        from models import storage
        st_cities = []
        for city in storage.all(City).values():
            if (self.id == city.state_id):
                st_cities.append(city)
        return st_cities
