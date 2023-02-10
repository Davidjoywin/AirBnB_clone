#!/usr/bin/python3
"""This is the base file of the model"""
import uuid
import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = None

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """This method update the update_at attribute"""
        self.updated_at = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def to_dict(self):
        """returns the dict representation of the obj"""
        return self.__dict__

