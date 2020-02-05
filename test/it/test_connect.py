import argparse
import mock

yamlStringSrv = """
mongo:
  host: mongodb+srv://cluster0-ctcov.mongodb.net/test
  username: m001-student
  password: m001-mongodb-basics
"""

yamlStringHostPort = """
mongo:
  host: localhost
  port: 27017
  username: m001-student
  password: m001-mongodb-basics
"""


class TestPyMongoClient:

    @mock.patch('argparse.ArgumentParser.parse_known_args',
                return_value=(argparse.Namespace(config="dummy.yml", common=None), argparse.Namespace()))
    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data=yamlStringSrv)
    def test_srv(self, mock_open, mock_args):

        from klein_config.config import EnvironmentAwareConfig
        config = EnvironmentAwareConfig()
        mock_open.assert_called_with('dummy.yml', 'r')

        from src.klein_mongo.mongo import connection
        assert isinstance(connection.host, list)
        assert len(connection.host) == 2

    @mock.patch('argparse.ArgumentParser.parse_known_args',
                return_value=(argparse.Namespace(config="dummy.yml", common=None), argparse.Namespace()))
    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data=yamlStringHostPort)
    def test_host_port(self, mock_open, mock_args):
        from klein_config.config import EnvironmentAwareConfig
        config = EnvironmentAwareConfig()
        mock_open.assert_called_with('dummy.yml', 'r')

        from src.klein_mongo.mongo import connection
        assert isinstance(connection.host, list)
        assert len(connection.host) == 2

