#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['pymongo', ]

setup_requirements = ['pymongo']

test_requirements = [ ]

setup(
    author="Boris Bauermeister",
    author_email='Boris.Bauermeister@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="A ETL tool",
    entry_points={
        'console_scripts': [
            'pyjobber=pyjobber.pyjobber:main',
            'pyjobber-version=pyjobber.pyjobber:version',
            'pyjobber-ping=pyjobber.pyjobber:ping',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pyjobber',
    name='pyjobber',
    packages=find_packages(include=[
                                    'pyjobber',
                                    'pyjobber.interfaces',
                                    'pyjobber.modules'
                                    ]),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/XeBoris/pyjobber',
    version='0.1.0',
    zip_safe=False,
)
