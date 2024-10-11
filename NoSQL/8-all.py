#!/usr/bin/env python3
from pymongo import MongoClient
"""List all documents in a collection.
"""


def list_all(mongo_collection):
    """
    List all documents in a collection.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The collection
     to list documents from.

    Returns:
    list: A list of documents in the collection, or an empty list
     if no documents exist.
    """
    # Fetch all documents from the collection
    documents = list(mongo_collection.find())

    return documents  # Return the list of documents
