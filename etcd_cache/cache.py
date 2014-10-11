from django.core.cache import BaseCache

from etcd import Client


class EtcdCache(BaseCache):
    CACHE_PREFIX = '/cache'

    def __init__(self, location, params):
        super(EtcdCache, self).__init__(params)

        hosts = params.get('HOSTS', None)
        if hosts is None:
            hosts = ['127.0.0.1', 4001]

        self.hosts = hosts

    def add(self, key, value, timeout=None, version=None):
        path = self._get_path(key, version=version)

        try:
            self.client.write(path, value, ttl=timeout, prevExist=False)
        except KeyError:
            return False
        else:
            return True

    def clear(self):
        try:
            self.client.delete(self.CACHE_PREFIX, recursive=True, dir=True)
        except KeyError:
            pass

    @property
    def client(self):
        if hasattr(self, '_client'):
            return self._client

        return Client(self.hosts, allow_reconnect=True)

    def delete(self, key, version=None):
        path = self._get_path(key, version=None)

        try:
            self.client.delete(path)
        except KeyError:
            pass

    def get(self, key, default=None, version=None):
        path = self._get_path(key, version=version)

        try:
            return self.client.read(path, consistent=True).value
        except KeyError:
            return default

    def _get_path(self, key, version=None):
        return '{}/{}'.format(self.CACHE_PREFIX, self.make_key(key, version=version))

    def set(self, key, value, timeout=None, version=None):
        path = self._get_path(key, version=None)

        self.client.set(path, value, ttl=timeout)
