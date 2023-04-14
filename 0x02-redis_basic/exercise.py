#/!usr/bin/env python3

""" exercise """

import redis
from typing import Union, Callable, Optional
from uuid import uuid4

UnionList = Union[str, bytes, int, float]

class Cache:
    """class Cache"""
    def __init__(self):
        """store instance of redis client and flush instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionList) -> str:
        """generate a random key, sore input data and return key"""
        my_key = str(uuid4())
        self._redis.mset({my_key: data})
        return my_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> UnionList:
        """ callable will be used to convert the data
        back to the desired format."""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        else:
            return data

    def get_str(self, data: str) -> str:
        """parametiza data as str"""
        return self.get(key, str)

    def get_int(self, data:str) -> int:
        """parametize data as int"""
        return self.get(key, int)


