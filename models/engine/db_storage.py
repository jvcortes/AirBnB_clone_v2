#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import os

class DBStorage:
    __engine = None
    __session = None


    def __init__(self):
        user = os.environ.get('HBNB_MYSQL_USER')
        password = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        database = os.environ.get('HBNB_MYSQL_DB')
        arg = "mysql+mysqldb://{}:{}@{}:3306/{}".format(user,
                                                        password,
                                                        host,
                                                        database)
        self.__engine = create_engine(arg, pool_pre_ping=True)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        classes = [User, State, City, Amenity, Place, Review]
        objects = {}
        if cls is None:
            for element in classes:
                _query = self.__session.query(element).all()
                for objecct in _query:
                    key = element.__name__ + "." + str(objecct.id)
                    objects[key] = objecct
        else:
            _query = self.__session.query(cls).all()
            for objecct in _query:
                key = cls.__name__ + "." + str(objecct.id)
                objects[key] = objecct

        return objects

    def new(self, obj):
        """Adds a new object in the database session

        Parameters:
            obj (Base): Object to introduce into the database session

        """
        self.__session.add(obj)

    def save(self):
        """Commits all changes into the database session."""
        self.__session.commit()

    def delete(self, obj):
        """Deletes an object from the database session.
        """
        if obj:
            obj.delete()
