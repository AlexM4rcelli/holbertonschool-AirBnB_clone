#!/usr/bin/python3
from models.__init__ import storage
import datetime
import uuid


class BaseModel:
    """
    This class defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initialize a instance"""
        if kwargs:
            self.id = str(uuid.uuid4())
            for name, value in kwargs.items():
                if name == 'created_at' or name == 'updated_at':
                    date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, name, date)
                else:
                    if name != '__class__':
                        setattr(self, name, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime().now()
            self.updated_at = datetime.datetime().now()
            storage.new(self)
    
    @property
    def id(self):
        return self._id

    def __str__(self):
        return f"{type(self)} ({self.__id}) {self.__dict__}"
    
    def save(self):
        """
        Updates the public instance attribute updated_at with 
        the current datetime
        """
        self.updated_at = datetime.datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        new = self.__dict__
        new["__class__"] = self.__class__.__name__
        new['created_at'] = self.created_at.isoformat()
        new['updated_at'] = self.updated_at.isoformat()
        return new
