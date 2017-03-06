#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

from publications_bootstrap import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-publications-bootstrap',
    version=__version__,
    author='Marc Bourqui',
    author_email='https://github.com/mbourqui',
    license='MIT',
    description='A Django app for managing scientific publications with a Bootstrap-powered UI.',
    long_description=README,
    url='https://github.com/mbourqui/django-publications-bootstrap',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.8.17',
        'Pillow>=2.4.0',
        'bibtexparser>=0.5.5',
        'django-countries>=4.0',
    ],
    zip_safe=False,
    keywords='django scientific publications citations references bibliography',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.5',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
