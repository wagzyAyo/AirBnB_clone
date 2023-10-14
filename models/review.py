#!/usr/bin/python3
"""This module contains Review class that inherit from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class attributes """
    place_id = ""
    user_id = ""
    text = ""
