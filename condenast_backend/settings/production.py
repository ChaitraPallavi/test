from condenast_backend.settings.base import *

# Changing db to mongo
from pymongo import MongoClient
uri = 'mongodb://username:password@host:port/dbname'
client = MongoClient(uri)
DB = client['dbname']

# Contentful credentials

SPACE_ID = 'contentful spaceID'
ACCESS_KEY = 'contentful access key'
