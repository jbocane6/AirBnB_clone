#!/usr/bin/python3
"""Serializes instances to a JSON file
and deserializes JSON file to instances."""
import json


class FileStorage():
    """Serializes instances to a JSON file
    and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        Args:
            obj (object): Object to get id.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        print("{}".format(key))
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as f:
            if self.__objects is not None:
                dict_json = {obj_key: obj_val.to_dict()for obj_key, obj_val
                             in self.__objects.items()}
                json.dump(dict_json, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, val in data.items():
                    val = eval(key.split(".")[0])(**val)
                    FileStorage.__objects[key] = val
        except FileNotFoundError:
            pass
