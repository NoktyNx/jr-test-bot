"""python setup.py file for project."""
from setuptools import setup, find_packages

setup(
    name='jr-bot',
    version='0.0.5',
    description='JR Testing Bot',
    author='Joe "NoktyN" Ro',
    author_email='jromano416@gmail.com',
    packages=find_packages('main', 'config'),
    package_dir={'': 'main'},
)
