# Klein Mongo

Module to allow simple instantiation of MongoDB from configuration

Host can be provided as a URI or an SRV record (see config.yml for an example)

## Python

Utilises python 3.7

### Ubuntu

```
sudo apt install python3.7
```

## Virtualenv

```
virtualenv -p python3.7 venv
source venv/bin/activate
echo -e "[global]\nindex = https://nexus.mdcatapult.io/repository/pypi-all/pypi\nindex-url = https://nexus.mdcatapult.io/repository/pypi-all/simple" > venv/pip.conf
pip install -r requirements.txt
```

### Testing
```bash
python -m pytest
```
For test coverage you can run:
```bash
pytest --cov-report term:skip-covered --cov src/ test/
```