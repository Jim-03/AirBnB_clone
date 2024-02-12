#!/usr/bin/python3
""" Module for reviews"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review."""
    def __init__(self, *args, **kwargs):
        """Constructs a review"""
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.text = kwargs.get('text', '')
