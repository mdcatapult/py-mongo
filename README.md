# Klein Mongo

Module to allow simple instantiation of MongoDB from configuration

See the [config.example.yml](./config.example.yml) for example configuration.

## Python

Uses python 3.7 but should be compatible with later versions.

## Usage

```python
connection = MongoConnection(config)
```

## Development
We use `virtualenv` for local development environments: `pip install virtualenv`.

Once installed, run:
```
virtualenv -p python3.11 venv
source venv/bin/activate
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

### License
This project is licensed under the terms of the Apache 2 license, which can be found in the repository as `LICENSE.txt`
