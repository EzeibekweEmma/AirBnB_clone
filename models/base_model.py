#!/usr/bin/python3
"""BaseModel for Airbnb Project"""
import uuid
from datetime import datetime
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """Base class for classes"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue

                if key in ['created_at', 'updated_at']:
                    setattr(self, key, self.string2time(value))
                    continue

                setattr(self, key, value)

        else:
            uuid_gen = uuid.uuid4()
            self.id = str(uuid_gen)
            now = datetime.now()
            self.created_at = now
            self.updated_at = now

            models.storage.new(self)

    @staticmethod
    def string2time(date_string):
        """Converts string to time"""
        return datetime.strptime(date_string, time)

    def __str__(self):
        """Returns string representation of an instance"""
        return("[{}] ({}) {}"
               .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Save an instance and set the updated time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns the attributes of the instance as a dict"""
        var = self.__dict__.copy()

        var['__class__'] = self.__class__.__name__
        var['created_at'] = self.created_at.isoformat()
        var['updated_at'] = self.updated_at.isoformat()
        return var
