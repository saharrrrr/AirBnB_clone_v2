#!/usr/bin/python3
"""Define the file storage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """class that serializes instances to a JSON file 
    and deserializes JSON file to instances.

    Attributes:
    __file_path: string - path to the JSON file.
    __objects: the dictionary that will store all objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects."""
        return FileStorage.__objects
    
    def new(self, obj):
        """ sets in __objects the obj with key."""
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__file_path, file)

    def reload(self):
        """deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path) as file:
                obj_key = json.load(file)
                for key in obj_key.values():
                    class_name = key["__class__"]
                    del key["__class"]
                    self.new(eval(class_name)(**key))
        except FileNotFoundError:
            return
