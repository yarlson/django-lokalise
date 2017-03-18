#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of django-lokalise.
# https://github.com/yarlson/django-lokalise

# Licensed under the BSD license:
# http://www.opensource.org/licenses/BSD-license
# Copyright (c) 2016, Yar Kravtsov <yarlson@gmail.com>

from setuptools import setup, find_packages
from lokalise import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
    "django",
    "requests",
]

setup(
    name='django-lokalise',
    version=__version__,
    description='Lokalise (https://lokalise.co) module for Django',
    long_description='''
Lokalise (https://lokalise.co) module for Django
''',
    keywords='Localization, Internationalization, Lokalise',
    author='Yar Kravtsov',
    author_email='yarlson@gmail.com',
    url='https://github.com/yarlson/django-lokalise',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Localization',
        'Topic :: Software Development :: Internationalization',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        "django>=1.8",
        "requests"
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'django-lokalise=django_lokalise.cli:main',
        ],
    },
)
