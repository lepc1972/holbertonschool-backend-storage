#!/usr/bin/env python3
""" Module PyMongo """


def schools_by_topic(mongo_collection, topic):
    """ show school list """
    return mongo_collection.find({"topics": topic})
