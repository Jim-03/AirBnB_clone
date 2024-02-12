#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """ Representa a state"""
    def __init__(self, *args, **kwargs):
        """ Constructs a state"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
