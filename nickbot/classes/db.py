import asyncio
import asyncio_redis


class DbHandler(object):

    human_readable_return = {0: 'Key {key} updated to {value}',
                             1: 'New key {key} set to {value}',
                             -1: 'Database error, message lost'}

    def __init__(self, config_redis):
        self.__connected = False
        asyncio.gather(self.connection(config_redis))

    @asyncio.coroutine
    def set(self, server_id, param, value):
        while not self.__connected:
            yield from asyncio.sleep(10)
        try:
            result = yield from self.__redis.hset(server_id, param, value)
            return result
        except Exception:
            return -1

    @asyncio.coroutine
    def get(self, server_id, param):
        while not self.__connected:
            yield from asyncio.sleep(10)
        try:
            result = yield from self.__redis.hget(server_id, param)
            return result
        except Exception:
            return -1

    @asyncio.coroutine
    def connection(self, config_redis):
        self.__redis = yield from asyncio_redis.Pool.create(
            host=config_redis['HOST'],
            port=int(config_redis['PORT']),
            poolsize=10)
        while True:
            try:
                ping = yield from self.__redis.ping()
                self.__connected = True
                yield from asyncio.sleep(10)
            except Exception:
                self.__connected = False
                yield from asyncio.sleep(10)

    @asyncio.coroutine
    def is_connected(self):
        return self.__connected
