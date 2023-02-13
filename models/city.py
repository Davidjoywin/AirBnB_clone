#!/usr/bin/python3
"""inherit from BaseModel"""

from .base_model import BaseModel


class City(BaseModel):
    """City Model
    attribute:
        string_id(string) - empty string: it will be the state.id
        name(string) - empty string
    """
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.name = ""
