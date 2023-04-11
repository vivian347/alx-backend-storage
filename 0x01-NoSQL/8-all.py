#!/usr/bin/env python3
""" 8-all """

import pprint

def list_all(mongo_collection):
    """ Python function that lists all documents in a collection """
    doc_list= []
    for doc in mongo_collection.find():
        doc_list.append(doc)

    return doc_list
