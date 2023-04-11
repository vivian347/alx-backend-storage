#!/usr/bin/env python3
""" inserts a new document in a collection based on kwargs """

def insert_school(mongo_collection, **kwargs):
    """9-insert"""
    return [mongo_collection.insert_one(kwargs).inserted_id]
