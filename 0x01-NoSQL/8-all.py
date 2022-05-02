#!/usr/bin/env python3
""" show all documents in a collection """


def list_all(mongo_collection):
    """ return a list, or empty list"""
    return [each for each in mongo_collection.find()]
