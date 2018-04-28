#!/usr/bin/env python

from distutils.core import setup

setup(name='screenshotapi',
      version='1.0',
      description='Python API Client for Screenshotapi.io',
      author='Doug Kerwin',
      author_email='dwkerwin@gmail.com',
      url='https://github.com/screenshotapi/screenshotapi-python',
      packages=['screenshotapi'],
      install_requires=open('requirements.txt').readlines()
     )
