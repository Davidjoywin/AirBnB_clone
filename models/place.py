#!/usr/bin/python3
"""inherit from BaseModel"""

from .base_model import BaseModel


class Place(BaseModel):
    """Place Model
    attribute:
        city_id(string) - empty string: it will be the City.id
        user_id(string) - empty string: it will be the User.id
        name(string) - empty string
        description(string) - empty string
        number_rooms(integer) - 0
        number_bathrooms:(integer) - 0
        max_guest(integer) - 0
        price_by_night(integer) - 0
        latitude(float) - 0.0
        longitude(float) - 0.0
        amenity_ids(list of string) - empty list: it will be the
        list of Amenity.id
        later
    """
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
