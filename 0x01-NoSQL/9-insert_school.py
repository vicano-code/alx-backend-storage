#!/usr/bin/env python3
"""
function that inserts a new document in a collection based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new school document in a collection

    Args:
    mongo_collection: the pymongo collection object
    kwargs: dict if items to insert

    Return: the new id
    """
    new_school = mongo_collection.insert_one(kwargs)

    return new_school.inserted_id
