#!/usr/bin/python3
"""This is the base file of the model"""
import uuid
import datetime
from models import storage


class BaseModel:
    """Custom base for all the classes in AirBnB console project

    Attributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: returns the class name, id and create the dictionary
        representations of the input values
        save(self): updates update_at attribute
        to_dict(self): returns the dictionary representation of the instance

    """
    def __init__(self, *args, **kwargs):
        """public instance attributes constructor

        Args:
            *args(args): arguments
            **kwargs(dict): attribute values
        """
        DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = value
                elif key == "id":
                    self.__dict__[key] = value
                else:
                    self.__dict__[key] = value
        storage.new(self)

    def __str__(self):
        """
        Returns the string representation of class name,
        id and dictionary represention of the object
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """This method update the update_at attribute"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns the dict representation of the obj"""
        dic = self.__dict__
        dic["__class__"] = self.__class__.__name__
        return dic
