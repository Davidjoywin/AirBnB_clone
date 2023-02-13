#!/usr/bin/python3
"""inherit from BaseModel"""

from .base_model import BaseModel


class Review(BaseModel):
    """Review Model
    attribute:
        place_id(string) - empty string: it will be the Place.id
        user_id(string) - empty string: it will be the User.id
        text(string) - empty string
    """
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
