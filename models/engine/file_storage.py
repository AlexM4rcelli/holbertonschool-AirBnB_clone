#!/usr/bin/python3

import json

class FileStorage:
    """
    Class that serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    def __init__(self, file_path):
        """Initialize a instance"""
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_list = {key: val for key, val in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            file.write(json.dumps(obj_list, default=str, indent=4))
    
    def reload(self): 
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                self.__objects = json.load(file)
        except:
            pass
