# Copyright (C) 2015 Bitquant Research Laboratories (Asia) Limited
# Released under the Simplified BSD License

from setuptools import setup


setup(
    name='bitcoin-price-api',
    version='0.0.5',
    author='Matthew Madurski',
    author_email='madurskimr@gmail.com',
    url='https://github.com/dursk/bitcoin-price-api',
    description="API's for bitcoin exchanges",
    long_description='''Price API's for bitcoin exchanges''',
    license='MIT',
    packages=['exchanges'],
    install_requires=['python-dateutil==2.4.2', 'requests==2.9.1'],
    use_2to3=True
)
