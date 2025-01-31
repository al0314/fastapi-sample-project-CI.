
import os
import redis

REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')  

r = redis.StrictRedis.from_url(REDIS_URL)

try:
    r.ping()  
    print("Successfully connected to Redis!")
except redis.ConnectionError:
    print("Failed to connect to Redis.")
