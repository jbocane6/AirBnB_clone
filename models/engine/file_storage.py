#!/usr/bin/python3
"""Serializes instances to a JSON file
and deserializes JSON file to instances."""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes instances to a JSON file
    and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        Args:
            obj (object): Object to get id.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            if FileStorage.__objects is not None:
                dict_json = {obj_key: obj_val.to_dict()for obj_key, obj_val
                             in FileStorage.__objects.items()}
                json.dump(dict_json, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, val in data.items():
                    val = eval(key.split(".")[0])(**val)
                    FileStorage.__objects[key] = val
        except FileNotFoundError:
            pass
