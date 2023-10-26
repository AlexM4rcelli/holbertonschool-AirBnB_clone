#!/usr/bin/python3
import models
from datetime import datetime
import uuid


class BaseModel:
    """
    This class defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initialize a instance"""
        if kwargs:
            for name, value in kwargs.items():
                if name == 'created_at' or name == 'updated_at':
                    date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, name, date)
                else:
                    if name != '__class__':
                        setattr(self, name, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        
    

    def __str__(self):
        sorted_dict = {}
        for key in sorted(self.__dict__):
            sorted_dict[f"{key}"] = self.__dict__[f"{key}"]
        return f"[{type(self).__name__}] ({self.id}) {sorted_dict}"
    
    def save(self):
        """
        Updates the public instance attribute updated_at with 
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        new = self.__dict__
        new["__class__"] = self.__class__.__name__
        for key, val in new.items():
            if isinstance(new[key], datetime):
                new[key] = val.isoformat()
            else:
                new[key] = val
        
        return new
