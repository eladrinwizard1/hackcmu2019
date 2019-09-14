import redis
import os
from typing import List

def init_conn():
    global rdb = redis.Redis(host='localhost', port=os.environ['REDIS_PORT'], \
                             db=0)

def add(urls: List[str], source: str) -> List[int]:
    add.ident += 1
    indents = []
    for url in urls:
        rdb.add(f'recipe:{add.ident}:url', url)
        rdb.add(f'recipe:{add.ident}:source', source)
        idents.append(add.ident)
    return idents
add.ident = 0

def get(ident: int) -> (str, str):
    url = rdb.get(f'recipe:{ident}:url')
    source = rdb.get(f'recipe:{ident}:source')
    return source, url
