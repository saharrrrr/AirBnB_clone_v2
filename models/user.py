#!/usr/bin/python3

from base_model import BaseModel

class User(BaseModel):
    """ this Class Represents User Informations.
    
    Attributes:
    Email => user email
    Password => user password
    First_name => user first name
    last_name => user last name """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
