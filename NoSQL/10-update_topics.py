#!/usr/bin/env python3
"""Provide a function for replacing the topics of matching schools."""


def update_topics(mongo_collection, name, topics):
    """Set topics for every school document matching the supplied name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}},
    )
