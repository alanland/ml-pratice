# coding: utf-8

import httplib2

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.data
collection = db.jiaoyou58

h = httplib2.Http(".cache")
h.add_credentials('name', 'password')


def getPage(url):
    global h
    resp, content = h.request(url)
    assert resp.status == 200
    return content


def saveSearchUrl(href):
    found = db.jiaoyou58url.find_one({'href': href})
    if found == None:
        db.jiaoyou58url.insert_one({'href': href})
        return True
    return False


def getPerson(href):
    return collection.find_one({'href': href})


def insertPerson(person):
    return collection.insert_one(person)
