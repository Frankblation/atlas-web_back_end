#!/usr/bin/env python3
"""
8-all - Module to interact with a
 MongoDB collection.

This module contains a function to
list all documents in a specified
MongoDB collection using PyMongo.

Functions:
----------
- list_all(mongo_collection): Returns a
 list of all documents in the collection.
"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """
    List all documents in a collection.

    Parameters:
    mongo_collection (pymongo.collection.Collection):
    The collection to list documents from.

    Returns:
    list: A list of documents in the collection,
    or an empty list if no documents exist.
    """
    # Fetch all documents from the collection
    documents = list(mongo_collection.find())

    return documents  # Return the list of documents
