#!/usr/bin/python3
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """
    Defines a database storage.

    Class attributes:
        __engine: database engine
        __session: database session

    Attributes:
        __engine: database engine
        __session: database session
    """

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
        if os.environ.get('HBNB_MYSQL_ENV') == 'test':
            Base.metadata.drop_all()


    def all(self, cls=None):
        """
        Gets all the records inside the database session.

        Parameters:
            cls (class): Custom class, if specified, the function will return
                only the records which are associated with the class.
        """
        classes = [City, State, User, Place, ]
        objects = {}

        if cls is None:
            for element in classes:
                for row in self.__session.query(element).all():
                    key = element.__name__ + "." + str(row.id)
                    objects[key] = row
        else:
            for row in self.__session.query(cls).all():
                key = cls.__name__ + "." + str(row.id)
                objects[key] = row

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
        """
        Deletes an object from the database session.

        Arguments:
            obj (Base): Object to delete
        """
        if obj:
            obj.delete()


    def reload(self):
        """Reloads the current database session."""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()
