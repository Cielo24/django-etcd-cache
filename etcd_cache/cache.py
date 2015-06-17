from django.core.cache import BaseCache
from etcd.client import Client


class EtcdCache(BaseCache):
    CACHE_PREFIX = '/cache'

    def __init__(self, location, params):
        super(EtcdCache, self).__init__(params)

        hosts = params.get('HOSTS', None)
        if hosts is None:
            hosts = ['127.0.0.1', 2379]

        self.hosts = hosts

    @property
    def host(self):
        """
        TODO: Handle cycling through all available hosts until our initial connection is established.
        Once established the etcd client will handle failover.
        :return:
        """
        return self.hosts[0]

    def add(self, key, value, timeout=None, version=None):
        path = self._get_path(key, version=version)

        try:
            self.client.node.create_only(path, value, ttl=timeout)
        except KeyError:
            return False
        else:
            return True

    def clear(self):
        try:
            self.client.node.delete(self.CACHE_PREFIX, recursive=True, dir=True)
        except KeyError:
            pass

    @property
    def client(self):
        if hasattr(self, '_client'):
            return self._client

        return Client(self.host)

    def delete(self, key, version=None):
        path = self._get_path(key, version=None)

        try:
            self.client.node.delete(path)
        except KeyError:
            pass

    def get(self, key, default=None, version=None):
        path = self._get_path(key, version=version)

        try:
            return self.client.node.get(path, consistent=True).value
        except KeyError:
            return default

    def _get_path(self, key, version=None):
        return '{}/{}'.format(self.CACHE_PREFIX, self.make_key(key, version=version))

    def set(self, key, value, timeout=None, version=None):
        path = self._get_path(key, version=None)

        self.client.set(path, value, ttl=timeout)
