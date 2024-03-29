# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='python-mass-mailer',
    version='0.1.0',
    description='Sample package description',
    long_description=readme,
    author='<author_name>',
    author_email='teckzy.co@example.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests'))
)
