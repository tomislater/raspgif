from __future__ import print_function
from setuptools import setup

import os

import raspgif

here = os.path.abspath(os.path.dirname(__file__))


setup(
    name='raspgif',
    version=raspgif.__version__,
    url='https://github.com/tomislater/raspgif',
    license='MIT License',
    author='Tomasz Święcicki',
    install_requires=[
    ],
    author_email='tomislater@gmail.com',
    description='Regional Atmospheric Soaring Prediction as a gif.',
    packages=['raspgif'],
    include_package_data=True,
    platforms='any',
)
