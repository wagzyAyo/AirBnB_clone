#!/usr/bin/python3
"""This module contains BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """The base Model class"""
    def __init__(self, *args, **kwargs):
        """initializing BaseModel class"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

        else:
            date_time = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, date_time))
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Define human readable of BaseModel Object
            should print: [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance:
        """
        dict_obj = {}
        dict_obj.update(self.__dict__)
        dict_obj.update({"__class__": self.__class__.__name__})
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()

        return dict_obj
