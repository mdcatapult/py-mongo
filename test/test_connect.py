import argparse
from unittest import mock

yamlStringHostPort = """
mongo:
  host: localhost
  port: 27017
  username: m001-student
  password: m001-mongodb-basics
  database: video
  collection: movies
  readPreference: secondary
"""


class TestPyMongoClient:

    @mock.patch('argparse.ArgumentParser.parse_known_args',
                return_value=(argparse.Namespace(config="dummy.yml", common=None), argparse.Namespace()))
    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data=yamlStringHostPort)
    def test_host_port(self, mock_open, mock_args):
        from klein_config import get_config
        config = get_config()
        mock_open.assert_called_with('dummy.yml', 'r')

        from src.klein_mongo import MongoConnection
        connection = MongoConnection(config)
        assert isinstance(connection.host, list)
        assert len(connection.host) == 2

