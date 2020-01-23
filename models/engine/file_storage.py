#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def delete(self, obj=None):
        """
        Deletes an object inside the storage.

        Args:
            obj (BaseModel): object to delete
        """
        if obj is None:
            return

        for key in self.__objects:
            if obj.id == self.__objects[key].id:
                del self.__objects[key]
                break
        self.save()

    def all(self, cls=None):
        """
            Returns a dictionary of BaseModel objects.

            Args:
                cls (str): Class to filter, if the class is found, a
                    dictionary with all the instances of the mentioned class is
                    returned.

            Return:
                dictionary containing all the object instances.
        """
        if cls:
            new_dict = {}
            for key in self.__objects:
                if cls.__name__ in key:
                    new_dict[key] = self.__objects[key]
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def close(self):
        """
        Reloads the file storage contents.
        """
        self.reload()
