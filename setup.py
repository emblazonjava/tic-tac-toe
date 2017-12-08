#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='TicTacToe',
    version='0.2',
    description='A tic-tac-toe game playable on RetroBrowser',
    author='Allison F',
    author_email='yetanotherallisonf@yahoo.com',
    url='https://github.com/allisonf/tic-tac-toe',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Topic :: Games/Entertainment',
        'Topic :: Terminals',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(exclude=['docs', 'tests']),

# TODO: Uncomment once RetroBrowser is in python package index
#    install_requires=["RetroBrowser"]
)
