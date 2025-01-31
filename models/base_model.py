#!/usr/bin/python3
"""
Module Name: models/base_model.py
Description: A definition of base class for other classes to inherit from
"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class definition for all hbnb models

    Attributes:
        id (str): A unique id for each instance created
        created_at (datetime): The date of creation of an instance
        updated_at (datetime): The date when an instance was updated last

    """
    __table_args__ = {'extend_existing': True}

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k in ('created_at', 'updated_at'):
                        v = datetime.fromisoformat(v)
                    setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dict_copy = self.__dict__.copy()
        if '_sa_instance_state' in dict_copy:
            del dict_copy['_sa_instance_state']
        return '[{}] ({}) {}'.format(cls, self.id, dict_copy)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage

        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        """Delete the current instance from the `FileStorage` (models.storage)
        with its delete method
        """
        from models import storage

        storage.delete(self)
