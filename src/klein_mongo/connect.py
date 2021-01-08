# -*- coding: utf-8 -*-
from pymongo import MongoClient as _MongoClient


def lazy_property(fn):
    '''Decorator that makes a property lazy-evaluated.
    '''
    attr_name = '_lazy_' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazy_property


class MongoConnection:

    def __init__(self, config):
        self.params = dict()

        self._db = None
        self._docs = None
        self.replicaSet = None

        if config.has('mongo.username'):
            self.params["username"] = config.get('mongo.username')

        if config.has('mongo.password'):
            self.params["password"] = config.get('mongo.password')

        if config.has('mongo.authSource'):
            self.params["authSource"] = config.get('mongo.authSource')

        elif config.has('mongo.database') and "username" in self.params:
            self.params["authSource"] = config.get('mongo.database')

        if config.has('mongo.authMechanism') and "password" in self.params:
            self.params["authMechanism"] = config.get('mongo.authMechanism')

        if isinstance(config.get('mongo.host'), str):
            if config.get('mongo.host').startswith("mongodb+srv"):
                self.host = [config.get('mongo.host')]
            else:
                self.host = [config.get('mongo.host'), int(config.get('mongo.port'))]
        else:
            self.host = [",".join(config.get("mongo.host")), int(config.get('mongo.port'))]

        if config.has('mongo.replicaSet'):
            self.replicaSet = config.get('mongo.replicaSet')

        if config.has('mongo.readPreference'):
            self.params["readPreference"] = config.get('mongo.readPreference')

        # Use cross language compatible UUID encoding as default. Can be overridden with
        # 'pythonLegacy', 'javaLegacy' or 'csharpLegacy' if required.
        # ref: https://api.mongodb.com/python/current/api/pymongo/mongo_client.html?
        self.params['uuidRepresentation'] = config.get('mongo.uuidRepresentation', 'standard')


    @lazy_property
    def client(self):
        c = _MongoClient(*self.host, replicaset=self.replicaSet, **self.params)
        return c


def get_connection(config):
    return MongoConnection(config)
