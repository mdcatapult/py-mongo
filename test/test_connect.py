import os
from unittest import mock
from klein_config import EnvironmentAwareConfig
from src.klein_mongo import MongoConnection, ConfigError
import pytest

config = EnvironmentAwareConfig({
    "mongo": {
        "host": ["mongo.domain.com"],
        "username": "me",
        "password": "secret",
    }
})


class TestPyMongoClient:

    def test_error(self):
        with pytest.raises(ConfigError) as e:
            MongoConnection(
                EnvironmentAwareConfig({
                    "mongo": {
                        "host": 23424,
                        "username": "me",
                        "password": "hello"
                    }
                }))
            assert str(e) == "mongo hosts must be string or list of strings"

    def test_connection(self):
        connection = MongoConnection(config)
        assert isinstance(connection.host, list)
        assert len(connection.host) == 2
        assert connection.host[0] == "mongo.domain.com"
        assert connection.host[1] == 27017

    @mock.patch.dict(os.environ, {"MONGO_HOST": "mongo0.domain.com,mongo1.domain.com,mongo2.domain.com"})
    def test_multiple_hosts(self):
        connection = MongoConnection(config)
        assert isinstance(connection.host, list)
        assert len(connection.host) == 2
        assert connection.host[0] == "mongo0.domain.com,mongo1.domain.com,mongo2.domain.com"
        assert connection.host[1] == 27017

    @mock.patch.dict(os.environ, {"MONGO_SRV": "true"})
    @mock.patch("pymongo.srv_resolver._SrvResolver.get_hosts",
                return_value=["mongo0.domain.com", "mongo1.domain.com", "mongo2.domain.com"])
    @mock.patch("pymongo.srv_resolver._SrvResolver.get_options", return_value="replicaSet=mongo")
    def test_srv(self, mock_hosts, mock_config):
        connection = MongoConnection(config)
        assert isinstance(connection.host, list)
        assert len(connection.host) == 1
        assert connection.host[0] == "mongodb+srv://mongo.domain.com"
        assert connection.params["username"] == "me"
        assert connection.params["password"] == "secret"
        assert connection.params["uuidRepresentation"] == "standard"
