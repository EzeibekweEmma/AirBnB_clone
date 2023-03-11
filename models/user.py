#!/usr/bin/python3
"""Module"""
from .base_model import BaseModel


class User(BaseModel):
    """Inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)
