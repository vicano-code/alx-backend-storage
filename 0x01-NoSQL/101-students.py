#!/usr/bin/env python3
"""
function that returns all students sorted by average score
"""
import pymongo


def top_students(mongo_collection):
    """
    returns all students sorted by average score

    mongo_collection: pymongo collection object form main func
    """
    tops = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
    return tops
