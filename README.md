# Klein Mongo

Module to allow simple instantiation of MongoDB from configuration

See the [config.example.yml](./config.example.yml) for example configuration.

## Python

Uses python 3.7 but should be compatible with later versions.

## Development
We use `virtualenv` for local development environments: `pip install virtualenv`.

Once installed, run:
```
virtualenv -p python3.7 venv
source venv/bin/activate
pip config set global.index https://nexus.mdcatapult.io/repository/pypi-all
pip config set global.index-url https://nexus.mdcatapult.io/repository/pypi-all/simple
pip config set global.trusted-host nexus.mdcatapult.io
pip install -r requirements.txt
```
Then configure your IDE to use the python interpreter located at `venv/bin/python`.
### Testing
```bash
python -m pytest
```
For test coverage you can run:
```bash
pytest --cov-report term:skip-covered --cov src/ test/
```