# -*- coding: utf-8 -*-
from klein_config import config
from .connect import MongoConnection

print(config)

connection = MongoConnection(config)

client = connection.client
db = connection.db
docs = connection.docs
