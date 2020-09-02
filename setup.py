#!/usr/bin/env python

# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup, find_packages

setup(
    version='0.1.0',
    name='name_placeholder',
    license='MIT License',
    description='',
    author='Firstname Lastname',
    author_email='my.email@protonmail.com',
    url='',
    packages=find_packages(include=['name_placeholder']),
    package_dir={'name_placeholder': 'name_placeholder'},
    entry_points={
        'console_scripts': [
            'name_placeholder=name_placeholder.__main__:main',
        ],
    },

    python_requires='>=3.6.0',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=open("requirements.txt", "r").readlines(),
    tests_require=['pytest==5.2.0'],
    setup_requires=['pytest-runner'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
