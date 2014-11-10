django-etc-cache
----------------

Use etcd as a cache backend for Django.

The advantage over memcached is that you get a distributed, fault-tolerant cache.


Testing
=======

This project includes a Django project and test suite.  To run the test suite,
have etcd running locally and accessible at port 4001 or set `ETCD_HOST` to one
or more, comma-delimited list of host:port pairs; for example:

```
export ETCD_HOST=192.168.10.137:4001,192.168.10.137:14001
```

etcd in a Docker container
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure to provide the docker host's IP to etcd in order for it to be properly accessible by the test suite:

```
export PUBLIC_IP=192.168.10.137
docker run -d -p 4001:4001 -p 7001:7001 coreos/etcd -peer-addr ${PUBLIC_IP}:7001 -addr ${PUBLIC_IP}:4001
```
