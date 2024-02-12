#!/usr/bin/python3
""" Module for an amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity."""
    def __init__(self, *args, **kwargs):
        """Constructor for an ameinty"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
