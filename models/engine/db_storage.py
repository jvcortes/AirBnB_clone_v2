#!/usr/bin/python3
from relationship_state import Base, State
from relationship_city import City
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
        
    def all(self, cls=None):
        classes = [User, State]#, City, Amenity, Place, Review] 
        Session = sessionmaker(bind=engine)
        objects = {}
        self.__session = Session()
        if cls is None:
            for element in classes:
                _query = session.query(element).all()
                for objecct in _query:
                    key = str(element) + "." + str(objecct.id)
                    objects[key] = objecct
            return objects
        else:
            _query = session.query(cls).all()
            for objecct in _query:
                key = str(element) + "." + str(objecct.id)
                objects[key] = objecct
        
            return objects
