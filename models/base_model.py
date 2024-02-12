#!/usr/bin/python3
"""Define The Base Class"""
import uuid
from datetime import datetime


class BaseModel:
    """The main class for the project
    all other classes will inherant from it."""
    def __init__(self):
        """Initialize a new BaseModel.
        Attributes:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        print(f"{self.__class__.__name__} {self.id} {self.__dict__}")

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance."""
        obj_dict = {}
        for key, value in self.__dict__.item():
            if isinstance(value, datetime):
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
