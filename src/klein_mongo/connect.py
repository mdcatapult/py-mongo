# copyright 2022 Medicines Discovery Catapult
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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


class ConfigError(Exception):
    pass


class MongoConnection:

    def __init__(self, config):
        self.params = {}

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

        host = config.get('mongo.host')
        srv = config.get('mongo.srv', False)
        use_srv = srv is True or (isinstance(srv, str) and srv.lower() in ['true', '1', 'yes'])
        if isinstance(host, str):
            if use_srv:
                self.host = [f"mongodb+srv://{host}"]
            else:
                self.host = [host, int(config.get('mongo.port', 27017))]
        elif isinstance(host, list):
            if use_srv:
                self.host = [f"mongodb+srv://{host[0]}"]
            else:
                self.host = [",".join(config.get("mongo.host")), int(config.get('mongo.port', 27017))]
        else:
            raise ConfigError("mongo hosts must be string or list of strings")

        if config.has('mongo.replicaSet'):
            self.replicaSet = config.get('mongo.replicaSet')

        self.params["readPreference"] = config.get('mongo.readPreference', 'secondaryPreferred')

        # Use cross language compatible UUID encoding as default. Can be overridden with
        # 'pythonLegacy', 'javaLegacy' or 'csharpLegacy' if required.
        # ref: https://api.mongodb.com/python/current/api/pymongo/mongo_client.html?
        self.params['uuidRepresentation'] = config.get('mongo.uuidRepresentation', 'standard')

        # There are some data with strings that cannot be handled by unicode
        # This may cause an error during query
        # Default this to ignore as there is no known good way to handle this other than ignoring corrupted data
        self.params['unicode_decode_error_handler'] = config.get('mongo.unicode_decode_error_handler', 'ignore')

    @lazy_property
    def client(self):
        c = _MongoClient(*self.host, replicaset=self.replicaSet, **self.params)
        return c


def get_client(config):
    return MongoConnection(config).client
