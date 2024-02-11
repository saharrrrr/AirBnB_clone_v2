#!/usr/bin/python3
"""Define BaseModel Class."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """The Basemodel of the HBnB Project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Attributes:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes."""

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or j == "updated_at":
                    self.__dic__[i] = datetime.strptime(j, time_format)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.save()

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        
        cls_name = self.__class__.__name__
        print(f"{cls_name} {self.id} {self.__dict__}")

    def save(self):
        """updates updated_at with the current datetime"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values"""

        dict1 = self.__dict__.copy()
        dict1["created_at"] = self.created_at.isoformat()
        dict1["updated_at"] = self.updated_at.isoformat()
        dict1["__class__"] = self.__class__.__name__
        return dict1
