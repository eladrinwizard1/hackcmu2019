import redis
import os
from typing import List

rdb = None

def init_conn():
    global rdb
    rdb = redis.Redis(host='localhost', port=os.environ['REDIS_PORT'], \
                      db=0)

def add(urls: List[str], source: str) -> List[int]:
    ident = rdb.incr('idcount')
    idents = []
    for url in urls:
        rdb.set(f'recipe:{ident}:url', url)
        rdb.set(f'recipe:{ident}:source', source)
        idents.append(ident)
    return idents

def get(ident: int) -> (str, str):
    url = rdb.get(f'recipe:{ident}:url').decode('utf-8')
    source = rdb.get(f'recipe:{ident}:source').decode('utf-8')
    return source, url
