#!/usr/bin/python3
""" module for a base class. """
import uuid
from datetime import datetime


class BaseModel:
    """ The base class for other classes. """
    def __init__(self, *args, **kwargs):
        """ initializes an object.
        Args:
            *args: unused arguments.
            **kwargs: arguments representing attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ The string representation of object.
        Returns:
            string representing the object.
        """
        name = self.__class__.__name__,
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """ Updates to the current date and time. """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ The dictionary representation of the object.
        Returns:
            obj_dict: the dictionary representation of the object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = type(self).__name__
        return obj_dict
