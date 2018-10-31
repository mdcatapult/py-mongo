# -*- coding: utf-8 -*-
from klein_config import config
from pymongo import MongoClient

params = dict()

if "username" in config['mongo']:
    params["username"] = config['mongo']['username']

if "password" in config['mongo']:
    params["password"] = config['mongo']['password']

if "database" in config['mongo'] and "username" in params:
    params["authSource"] = config['mongo']['database']

if "authMechanism" in config['mongo'] and "password" in params:
    params["authMechanism"] = config['mongo']['authMechanism']


client = MongoClient(config['mongo']['host'], config['mongo'].getint('port'), **params)

db = client[config['mongo']['database']]
docs = db[config['mongo']['collection']]