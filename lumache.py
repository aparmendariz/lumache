# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:06:39 2023

@author: AArmendarizPacheco
"""

def get_random_ingredients(kind=None):
    return ["eggs", "bacon", "spam"]

def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]

    """
    return ["shells", "gorgonzola", "parsley"]

class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass