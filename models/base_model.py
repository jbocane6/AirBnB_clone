#!/usr/bin/python3
"""Defines all common attributes/methods for other classes."""
import uuid
from datetime import datetime


class BaseModel():
    """Defines all common attributes/methods."""

    def __init__(self):
        """Defines all common attributes."""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns info about class."""
        return "[<class name>] (<{}>) <{}>".format(self.id, self.__dict__)

    def save(self):
        """Assigns with the current datetime when an instance is created and
        it will be updated every time the object is changed"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = type(self).__name__
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        return base_dict
