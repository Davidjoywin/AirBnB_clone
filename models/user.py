#!/usr/bin/python3
"""Inherit from BaseModel"""


from .base_model import BaseModel


class User(BaseModel):
    """Class User that inherit from BaseModel"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
