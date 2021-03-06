#!/usr/bin/python3
"""This is the state class"""
import os
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.environ["HBNB_TYPE_STORAGE"] != "db":
        @property
        def cities(self):
            """
            Returns the list with all the cities associated with a state.
            """

            associated_cities = []
            all_cities = models.storage.all(models.city.City)

            for city in all_cities:
                if all_cities[city].state_id == self.id:
                    associated_cities.append(all_cities[city])

            return associated_cities
    else:
        cities = relationship("City", backref="states")
