#!/usr/bin/python3
"""serializes instances to a JSON file and deserialize
JSON file to instances"""

import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file
    to instances"""

    __file_path = "model.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__
        self.__objects[f"{key}.{obj.id}"] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as file_to_write:
            file_to_write.write(json.dumps(self.__objects))

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as read_file:
                self.__objects = json.load(read_file)
        except Exception:
            pass
