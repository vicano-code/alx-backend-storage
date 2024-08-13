#!/usr/bin/env python3
"""
function that lists all documents in a mongodb collection
"""
import pymongo


def list_all(mongo_collection) -> list:
    """lists all documents"""
    documents: list = []
    for document in mongo_collection.find():
        documents.append(document)

    return documents
