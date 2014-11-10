#!/usr/bin/env python 
import os

from setuptools import setup

SCRIPT_DIR = os.path.dirname(__file__)
if not SCRIPT_DIR:
        SCRIPT_DIR = os.getcwd()

README = open(os.path.join(SCRIPT_DIR, 'README.md')).read()


version = '0.0.1'

install_requires = [
    'python-etcd==0.3.2',
]

test_requires = [
    'mock',
]

setup(name='django-etcd-cache',
    version=version,
    description="Use etcd as a Django cache backend",
    long_description=README,
    keywords='cache django etcd',
    author='Roberto Aguilar',
    author_email='roberto.c.aguilar@gmail.com',
    url='http://github.com/Cielo24/django-etc-cache',
    license='LICENSE.txt',
    packages=['etcd_cache'],
    zip_safe=False,
    install_requires=install_requires,
    tests_require=test_requires,
)
