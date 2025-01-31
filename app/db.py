import os
from pymongo import MongoClient

MONGO_URL = os.getenv('MONGO_URL')
REDIS_URL = os.getenv('REDIS_URL')

client = MongoClient(MONGO_URL)
