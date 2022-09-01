"""
base_model.py
It defines all common attributes/methods for other classes
"""

from datetime import datetime
import uuid
import models

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{ self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return my_dict
