"""
base_model.py
It defines all common attributes/methods for other classes
"""

from datetime import datetime
import uuid
import models

class BaseModel:
    """ initialization method """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ printing string formated output """
        return f"[{ self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ saves the object """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returning a dictionary format """ 
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return my_dict
