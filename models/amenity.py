#!/usr/bin/python3
"""inherit from BaseModel"""

from .base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Model
    attribute:
        name(string) - empty string
    """
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.name = ""
