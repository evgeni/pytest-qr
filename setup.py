#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
setup.py for pytest-qr
"""

import os
import codecs
from setuptools import setup


def read(fname):
    """
    read file and return its contents
    """
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-qr',
    version='0.1.0',
    author='Evgeni Golov',
    author_email='evgeni@golov.de',
    maintainer='Evgeni Golov',
    maintainer_email='evgeni@golov.de',
    license='MIT',
    url='https://github.com/evgeni/pytest-qr',
    description='pytest plugin to generate test result QR codes',
    long_description=read('README.rst'),
    py_modules=['pytest_qr'],
    python_requires='>=3.6',
    install_requires=['pytest>=3.5.0', 'qrcode'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'qr = pytest_qr',
        ],
    },
)
