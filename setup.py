#!/usr/bin/env python 
import os

from distutils.core import setup

SCRIPT_DIR = os.path.dirname(__file__)
if not SCRIPT_DIR:
        SCRIPT_DIR = os.getcwd()


setup(name='django-etc-cache',
      version='0.0.1',
      description='Using ',
      author='Roberto Aguilar',
      author_email='roberto.c.aguilar@gmail.com',
      packages=['etcd_cache'],
      long_description=open('README.md').read(),
      url='http://github.com/Cielo24/django-etc-cache',
      license='LICENSE.txt',
)
