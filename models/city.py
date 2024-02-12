#!/usr/bin/python3
""" module for a city"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Represents the city"""
    def __init__(self, *args, **kwargs):
        """Constructor for a city"""
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', '')
        self.name = kwargs.get('name', '')
