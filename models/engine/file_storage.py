#!/usr/bin/python3
""" Serializes and deserializes instances in JSON."""
import json
from ..base_model import BaseModel
from models.user import User


class FileStorage:
    """ Represents how a file is stored."""
    def __init__(self):
        """ The constructor."""
        self.__file_path = ""
        self.__objects = {}

    def all(self):
        """ Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as FILE:
            json.dump(obj_dict, FILE)

    def reload(self):
        """ Deserializes an existing JSON file to __objects"""
        try:
            with open(self._FileStorage__file_path) as fopen:
                for anOpen in json.load(fopen).values():
                    className = anOpen["__class__"]
                    del anOpen["__class__"]
                    cls = {"User": User, "BaseModel": BaseModel}[className]
                    self.new(cls(**anOpen))
        except FileNotFoundError:
            return
