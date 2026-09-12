#!/usr/bin/env python3
"""Rank students by their average topic score using aggregation."""


def top_students(mongo_collection):
    """Return students ordered from highest to lowest average score."""
    pipeline = [
        {
            "$addFields": {
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}},
    ]
    return list(mongo_collection.aggregate(pipeline))
