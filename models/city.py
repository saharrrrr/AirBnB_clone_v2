#!/usr/bin/python3
"""Define the city class."""
from models.base_model import BaseModel

class City(BaseModel):
    """Repersent the city.
    Attributes:
    state_id: the city id.
    name: city name.
    """
    state_id = ""
    name = ""
    
