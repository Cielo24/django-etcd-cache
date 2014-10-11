"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import time

from django.core.cache import cache
from django.test import TestCase

cache.CACHE_PREFIX='/testcache'


class CacheTestCase(TestCase):
    """
    These are integration tests that require a running etcd cluster, even if
    it's a single node
    """
    def tearDown(self):
        cache.clear()

    def test_add(self):
        """
        Ensure trying to add the same key a second time fails
        """
        self.assertEqual(True, cache.add('test', 'foo'))
        self.assertEqual(False, cache.add('test', 'foo'))

    def test_clear(self):
        cache.add('foo', 1)
        cache.add('bar', 1)

        cache.clear()

        self.assertEqual(None, cache.get('foo'))
        self.assertEqual(None, cache.get('bar'))

    def test_delete(self):
        cache.add('test', 'foo')
        cache.delete('test')

        self.assertEqual(None, cache.get('test'))

    def test_delete_non_existent(self):
        cache.delete('test')

        self.assertEqual(None, cache.get('test'))

    def test_get(self):
        cache.add('test', 'foo')

        self.assertEqual('foo', cache.get('test'))

    def test_get_non_existent(self):
        self.assertEqual(None, cache.get('test'))

    def test_get_non_existent_2(self):
        # set a different key than the one being fetched below
        cache.set('foo', 1)

        self.assertEqual(None, cache.get('test'))

    def test_get_non_existent_returns_default(self):
        self.assertEqual('hi', cache.get('test', default='hi'))

    def test_set(self):
        cache.set('test', 'foo')

        self.assertEqual('foo', cache.get('test'))

    def test_set_existent(self):
        cache.set('test', 'foo')
        cache.set('test', 'bar')

        self.assertEqual('bar', cache.get('test'))

    def test_set_ttl(self):
        """
        slow ....
        """
        cache.set('test', 'foo', timeout=1)

        self.assertEqual('foo', cache.get('test'))

        time.sleep(1.5)  # has to be slightly more than the timeout

        self.assertEqual(None, cache.get('test'))
