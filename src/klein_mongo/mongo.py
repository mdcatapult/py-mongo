# -*- coding: utf-8 -*-
from klein_config import config
from pymongo import MongoClient

params = dict()

if config.has('mongo.username'):
    params["username"] = config.get('mongo.username')

if config.has('mongo.password'):
    params["password"] = config.get('mongo.password')

if config.has('mongo.authSource'):
    params["authSource"] = config.get('mongo.authSource')
elif config.has('mongo.database') and "username" in params:
    params["authSource"] = config.get('mongo.database')

if config.has('mongo.authMechanism') and "password" in params:
    params["authMechanism"] = config.get('mongo.authMechanism')


client = MongoClient(config.get('mongo.host'), int(config.get('mongo.port')), **params)

db = client[config.get('mongo.database')]
docs = db[config.get('mongo.collection')]