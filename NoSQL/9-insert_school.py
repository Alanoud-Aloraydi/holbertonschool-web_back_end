#!/usr/bin/env python3
"""Provide a function for inserting a school document into MongoDB."""


def insert_school(mongo_collection, **kwargs):
    """Insert a document built from keyword arguments and return its ID."""
    return mongo_collection.insert_one(kwargs).inserted_id
