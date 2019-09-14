import redis
import os
from typing import List

rdb = None

def init_conn():
    global rdb
    rdb = redis.Redis(host='localhost', port=os.environ['REDIS_PORT'], \
                      db=0)

def add(urls: List[str], source: str, extras=None) -> List[int]:
    idents = []
    for count, url in enumerate(urls):
        ident = rdb.incr('idcount')
        rdb.set(f'recipe:{ident}:url', url)
        rdb.set(f'recipe:{ident}:source', source)
        if extras is not None:
            for extra in extras:
                rdb.set(f'recipe:{ident}:{extra}', extras[extra][count])
        idents.append(ident)
    return idents

def get(ident: int) -> (str, str):
    url = rdb.get(f'recipe:{ident}:url').decode('utf-8')
    source = rdb.get(f'recipe:{ident}:source').decode('utf-8')
    extras = dict()
    extras['image'] = rdb.get(f'recipe:{ident}:image', b'null').decode('utf-8')
    extras['desc'] = rdb.get(f'recipe:{ident}:desc', b'null').decode('utf-8')
    return source, url, extras
