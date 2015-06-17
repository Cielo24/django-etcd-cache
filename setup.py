#!/usr/bin/env python 
import os

from setuptools import setup
from pip.req import parse_requirements

SCRIPT_DIR = os.path.dirname(__file__)
if not SCRIPT_DIR:
        SCRIPT_DIR = os.getcwd()

README = open(os.path.join(SCRIPT_DIR, 'README.md')).read()


version = '0.0.1'

app_path = os.path.dirname(__file__)
pip_reqs = parse_requirements(os.path.join(app_path, 'requirements.txt'))
install_requires = [str(ir.req) for ir in pip_reqs]
print(install_requires)
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
