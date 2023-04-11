#!/usr/bin/env python3

""" 11-school* """

def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    school_list = []

    for doc in mongo_collection.find({"topics" : topic}):
        school_list.append(doc)

    return school_list
